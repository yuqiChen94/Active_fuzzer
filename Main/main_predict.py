#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from sklearn.externals import joblib
import numpy as np
import time

origin_model1 = joblib.load("model/LIT101_diff30_rfr120.pkl")
temp_vector = []

while True:
    t = 0
    s1old = np.loadtxt('stage1old.txt')
    s1old = s1old.tolist()
    y_old = origin_model1.predict(s1old)
    for index in range(len(s1old)):
        temp = s1old[:]
        if temp[index] == 0:
            temp[index] = 1
        elif temp[index] == 1:
            temp[index] = 0
        y_new = origin_model1.predict(temp)
        if abs(y_new - y_old) >= t:
            t = abs(y_new - y_old)
            index_temp = index
            temp_vector = temp[:]
    stage1new = temp_vector[:]
    np.savetxt('stage1new.txt',stage1new)
    np.savetxt('bit_alter1.txt',index_temp)
    time.sleep(5)
