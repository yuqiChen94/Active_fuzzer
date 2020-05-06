#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import time
from sklearn.metrics import r2_score
import xgboost as xgb


def train_rfr(x, y):
    model_rfr = RandomForestRegressor(n_estimators=100)
    model_rfr.fit(x, y)
    return model_rfr


def train_linear(x, y):
    model_linear = LinearSVR(C=1, tol=1e-5,max_iter=1000)
    model_linear.fit(x, y)
    return model_linear


def train_xgb(x,y):
    model_xgb = xgb.XGBRegressor(max_depth=10, learning_rate=0.1, n_estimators=100, silent=False)
    model_xgb.fit(x, y)
    return model_xgb


def train_gbdt(x, y):
    model_gbdt = GradientBoostingRegressor(
        loss='ls'
        , learning_rate=0.1
        , n_estimators=100
        , subsample=0.8
        , min_samples_split=2
        , min_samples_leaf=1
        , max_depth=10
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

sensor = 'DPIT301'
X = np.load(sensor + '_bits_90min.npy')
y = np.loadtxt(sensor + '_value5_90min.txt')
# X_test = np.load('LIT401_bits_test.npy')
# y_test = np.loadtxt('LIT401_diff30_test.txt')
X_train = X[6000:8400]
y_train = y[6000:8400]
X_test = X[:4000]
y_test = y[:4000]
print 'complete loading data'
model = train_linear(X_train,y_train)
joblib.dump(model,sensor+'_linear_90min.pkl')
# model = train_gbdt(X_train,y_train)
# joblib.dump(model,sensor+'_GBDT_90min.pkl')
print 'complete training'
prediction = model.predict(X_test)
print 'model_score', r2_score(y_test,prediction)

# sensor = 'FIT401'
# method = 'GBDT'
# time_list = ['40']
# X = np.load('vector/0718total.npy')[2000:]
# y = np.loadtxt('vector/0718'+sensor+'_value5.txt')[2000:]
# for i in range(6):
#     X_train = X[:60*int(time_list[i])]
#     print len(X_train)
#     y_train = y[:60*int(time_list[i])]
#     if method == 'GBDT':
#         model = train_gbdt(X_train,y_train)
#     if method == 'linear':
#         model = train_linear(X_train, y_train)
#     joblib.dump(model,'model/'+sensor+'/'+sensor+'_'+method+'_'+time_list[i]+'min.pkl')
# y_predict = []

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
# plt.figure()
# plt.plot(range(len(y_test)),y_test,'b',label = 'real_test')
# plt.plot(range(len(y_test)),prediction,'r',label = 'predict_test')
# #plt.text(900,5,'r2_score='+str(float('%.4f' % mean[0])),size=15,alpha=1.0,color='g')
# plt.legend()
# plt.show()
