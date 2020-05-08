#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import time
from sklearn.metrics import r2_score


def train_rfr(x, y):
    model_rfr = RandomForestRegressor(n_estimators=100)
    model_rfr.fit(x, y)
    return model_rfr


def train_SVR(x, y):
    model_svr = SVR(kernel='linear', C=1, gamma=0.01)
    model_svr.fit(x, y)
    return model_svr

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


def split_data(data, rate=0.25):
    return np.array(data[:int(len(data)*rate)]), np.array(data[int(len(data)*rate):])


def predict_once(x, model_once):
    result = model_once.predict(x)
    return result


# X_t = np.loadtxt('vector/0429LIT101_corr_bits.txt')
# y_t = np.loadtxt('vector/0429LIT101_y_diff30.txt')

a = time.time()
X_train = np.loadtxt('vector/0718train.txt')
X_test = np.loadtxt('vector/0718test.txt')
print (len(X_train))
y_train = np.loadtxt('vector/0718LIT101_train.txt')
y_test = np.loadtxt('vector/0718LIT101_test.txt')
print 'load time:',time.time()-a

#
# X = np.loadtxt('vector/0710stage1_whole.txt')
# y = np.loadtxt('vector/0710LIT101_y_diff30.txt')
# X_train, X_test = split_data(X)
# np.savetxt('vector/0710stage1_train.txt',X_train)
# y_train, y_test = split_data(y)
# np.savetxt('vector/0710LIT101_diff30_train.txt',y_train)
# np.savetxt('stage4test0.txt',X_test,fmt='%d')
# np.savetxt('LIT401test0.txt',y_test)
# np.savetxt('stage4_batch0.txt',X_train,fmt='%d')
# np.savetxt('LIT401_batch0.txt',y_train)

'''real value'''
# y_real = np.loadtxt('vector/0703LIT301_y_diff30.txt')
# y_realtrain, y_realtest = split_data(y_real)
# X_test = X[8000:]
# y_test = y[8000:]
# for i in range(3,6):


# for j in range(6):
#     model = train_SVR(X[1800:1800+(j+1)*600], y[1800:1800+(j+1)*600])
#     plt.figure()
#     plt.plot(range(len(y[1800:1800+(j+1)*600])),y[1800:1800+(j+1)*600], 'b', label='real_train')
#     plt.legend()
#     plt.show()
#     predict_y = model.predict(X_test)
#     print j,r2_score(y_test,predict_y)
#     plt.figure()
#     plt.plot(range(len(y_test)), y_test, 'b', label='real_test')
#     plt.plot(range(len(y_test)), predict_y, 'r', label='predict_test')
#     plt.legend()
#     plt.show()

model = train_SVR(X_train,y_train)
joblib.dump(model, "model/0718LIT101_diff30_linear.pkl")

y_predict = []

'''predict based on difference'''
'''diff_train'''
# y_predict.append(X_train[0][-1]+predict_once([X_train[0]],model))
# for i in range(1,len(X_train)):
#     X_train[i][-1] = y_predict[i-1]
#     y_predict.append(X_train[i][-1] + predict_once([X_train[i]], model))


'''diff_test'''
# y_predict.append(X_test[0][-1]+predict_once([X_test[0]],model))
# for i in range(1,len(X_test)):
#     X_test[i][-1] = y_predict[i-1]
#     y_predict.append(X_test[i][-1] + predict_once([X_test[i]], model))
# plt.plot(range(len(y_realtest)),y_realtest,'r',label = 'real_test')
# plt.plot(range(len(y_test)),y_predict,'b',label = 'predict_test')

'''predict based on value'''
'''value_train'''
# y_predict.append(predict_once([X_train[0]],model))
# for i in range(1,len(X_train)):
#     X_train[i][-1] = y_predict[i-1]
#     y_predict.append(predict_once([X_train[i]], model))
# plt.plot(range(len(y_realtrain)),y_realtrain,'r',label = 'real_train')
# plt.plot(range(len(y_train)),y_predict,'b',label = 'predict_train')

'''value_test'''
# y_predict.append(predict_once([X_test[0]],model))
# for i in range(1,len(X_test)):
#     X_test[i][-1] = y_predict[i-1]
#     y_predict.append(predict_once([X_test[i]], model))
# # plt.plot(range(len(y_realtest)),y_realtest,'r',label = 'real_test')
# plt.plot(range(len(y_test)),y_predict,'b',label = 'predict_test')

# plt.grid()
# plt.legend()
# # plt.savefig("figure/LIT101_value20_SVR.png")
# plt.show()

'''predict directly'''
a = model.predict(X_test)
plt.figure()
plt.plot(range(len(y_test)),y_test,'b',label = 'real_test')
plt.plot(range(len(y_test)),a,'r',label = 'predict_test')
plt.legend()
plt.show()
# plt.figure()
# plt.plot(range(len(y_test)),y_test,'b',label = 'real_test')
# plt.legend()
# plt.show()
# plt.figure()
# plt.plot(range(len(y_train)),y_train,'b',label = 'real_train')
# plt.legend()
# plt.show()
# b = model.predict(X_train)
# plt.figure()
# plt.plot(range(len(y_train)), y_train, 'b', label='real_train')
# plt.plot(range(len(y_train)), b, 'r', label='predict_train')
# plt.legend()
# plt.savefig("figure/LIT101_value20_rfr.png")
