#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from sklearn.externals import joblib
import numpy as np
import time
from preprocess import *
from AL_utils import *
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import LinearSVR


def save(filename, contents):
	fh = open(filename, 'w')
	fh.write(contents)
	fh.close()


def read(filename):
	fh = open(filename, 'r')
	contents = fh.read()
	fh.close()
	return contents


# import model
sensor = 'LIT401'
method = 'GBDT'
algorithm = 'EMCM'
model = joblib.load(sensor+'/origin/'+sensor+'_'+method+'_40min.pkl')
# import first batch
bits = np.load(sensor+'/origin/'+sensor+'_'+'bits_40min.npy')
label = np.loadtxt(sensor+'/origin/'+sensor+'_'+ 'diff30_40min.txt')
# testx = np.load(sensor+'/origin/'+sensor+'_'+'bits_test.npy')
# testy = np.loadtxt(sensor+'/origin/'+sensor+'_'+'diff30_test.txt')
#state:accept,modify
state_list = '0 0'
save('zmq/stage_states.txt', state_list)
if algorithm == 'EMCM':
	block_size=int(np.shape(bits)[0]**(1/3))+1
	if method == 'linear':
		bootstrap_linear_model(bits,label,block_size,4)
	if method == 'GBDT':
		bootstrap_GBDT_model(bits, label, block_size, 4)
	model_list = ['model/bootstrap_' + method + '_example0.pkl', 'model/bootstrap_' + method + '_example1.pkl',
				  'model/bootstrap_' + method + '_example2.pkl',
				  'model/bootstrap_' + method + '_example3.pkl']
vector = bits.tolist()
pv = label.tolist()
count = 0
print 'done loading'

# a = model.predict(testx)
# plt.figure()
# plt.plot(range(len(testy)), testy, 'b', label='real_test')
# plt.plot(range(len(testy)), a, 'r', label='predict_test')
# plt.legend()
# plt.show()


def train_gbdt(x, y):
	model_gbdt = GradientBoostingRegressor(
		loss='ls'
		, learning_rate=0.1
		, n_estimators=100
		, subsample=0.8
		, min_samples_split=2
		, min_samples_leaf=1
		, max_depth=50
		, init=None
		, random_state=None
		, max_features=None
		, alpha=0.9
		, verbose=0
		, max_leaf_nodes=None
		, warm_start=False
	)
	model_gbdt.fit(x,y)
	return model_gbdt


def train_linear(x, y):
	model_linear = LinearSVR(C=1, tol=1e-5,max_iter=1000)
	model_linear.fit(x, y)
	return model_linear


def search(vector,model):
	vector_list = []
	v_list = []
	y0 = model.predict([vector[0]])
	for i in vector:
		y = model.predict([i])
		diff = abs(y-y0)
		v_list.append(diff)
	temp_list = v_list[:]
	temp_list.sort(reverse=True)
	for i in range(10):
		vector_list.append(vector[v_list.index(temp_list[i])])
	return vector_list


while True:
	try:
		capture_flag1 = read('zmq/capture_flag1.txt')
		capture_flag2 = read('zmq/capture_flag2.txt')
		capture_flag3 = read('zmq/capture_flag3.txt')
		capture_flag4 = read('zmq/capture_flag4.txt')
		if capture_flag1 == capture_flag2 == capture_flag3 == capture_flag4 == 'True':
			state_list = '1 0'
			save('zmq/stage_states.txt', state_list)
			s1old = np.loadtxt('zmq/stage1old.txt')
			s1old = s1old.tolist()
			s2old = np.loadtxt('zmq/stage2old.txt')
			s2old = s2old.tolist()
			s3old = np.loadtxt('zmq/stage3old.txt')
			s3old = s3old.tolist()
			s4old = np.loadtxt('zmq/stage4old.txt')
			s4old = s4old.tolist()
			old_vector = s1old+s2old+s3old+s4old
			#storage all the modified vector according to search algorithm
			vector_temp = []
			for i in range(2752):
				temp = bit_flip(old_vector, i)
				if i == 583:
					temp = bit_flip(temp, 1279)
				if i == 1279:
					temp = bit_flip(temp, 583)
				if i == 1955:
					temp = bit_flip(temp, 1959)
				if i == 1959:
					temp = bit_flip(temp, 1955)
				if i == 2643:
					temp = bit_flip(temp, 2647)
				if i == 2647:
					temp = bit_flip(temp, 2643)
				vector_temp.append(temp)
			vector_temp = np.array(vector_temp)
			if algorithm == 'EMCM':
				if method == 'GBDT':
					vector_list = EMCM_GBDT(model, 4, model_list, len(vector_temp), vector_temp, 100)
				if method == 'linear':
					vector_list = EMCM_linear(model, 4, model_list, len(vector_temp), vector_temp)
			if algorithm == 'behavior':
				vector_list = search(vector_temp, model)
			#start modifying packets
			for i in range(len(vector_list)):
				state_list = '0 1'
				np.savetxt('zmq/newvector.txt', vector_list[i], fmt='%d')
				time.sleep(2)
				print 'start modifying packets'
				save('zmq/stage_states.txt', state_list)
				time.sleep(30)
				print 'modifying end'
				temp_pv = read('zmq/pv1.txt')
				temp_pv = float('%.4f' % temp_pv)
				print 'pv_diff', temp_pv
				for j in range(10):
					vector.append(vector_list[i])
					pv.append(temp_pv)
			print 'start_training'
			if method == 'GBDT':
				model = train_gbdt(vector, pv)
			if method == 'linear':
				model = train_linear(vector, pv)
			joblib.dump(model, sensor + '/' + method + '/' + sensor + '_' + method + '_'+algorithm+'_' + str(count) + ".pkl")
			count += 1
			print 'rount',count
			print 'training over'
			state_list = '0 0'
			save('zmq/stage_states.txt', state_list)
			np.save(sensor + '/' + method + '/' + sensor + '_new_' + method + '_' + algorithm + '.npy', vector)
			np.savetxt(sensor + '/' + method + '/' + sensor + '_new_' + method + '_' + algorithm + '_diff30.txt', pv,
					   fmt='%.4f')
		else:
			time.sleep(1)
	except KeyboardInterrupt:
		state_list = '0 0'
		save('zmq/stage_states.txt', state_list)
		print 'stop modifying and prediction'
		break

