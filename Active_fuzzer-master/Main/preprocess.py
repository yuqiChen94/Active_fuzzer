from __future__ import division
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
import numpy as np
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import random
import math


def train_gbdt(x, y):
    model_gbdt = GradientBoostingRegressor(
        loss='ls'
        , learning_rate=0.1
        , n_estimators=100
        , subsample=0.8
        , min_samples_split=2
        , min_samples_leaf=1
        , max_depth=7
        , init=None
        , random_state=None
        , max_features=None
        , alpha=0.9
        , verbose=0
        , max_leaf_nodes=None
        , warm_start=False
    )
    model_gbdt.fit(x, y)
    return model_gbdt



def bootstrap_con(X,y,block_size):
    shape=np.shape(X)
    num_item =shape[0]
    vector_size=shape[1]
    num_blocks = num_item //block_size
    if num_blocks * block_size < num_item:
        num_blocks += 1
    new_X=np.zeros(shape=(num_blocks*block_size,vector_size))
    new_y=np.zeros(shape=num_blocks*block_size)
    max_block_index = num_item - block_size
    for i in range(num_blocks):
        index=random.randint(0,max_block_index)
        # print index
        # print X[index:index+block_size]
        new_X[i*block_size:(i+1)*block_size]=X[index:index+block_size]
        new_y[i * block_size:(i + 1) * block_size] = y[index:index + block_size]
    return new_X,new_y

# According to book "Advanced Data Analysis from an Elementary Point of View", the size of block should be n^(1/3)
# block_size=int(np.shape(X)[0]**(1/3))+1
# According to paper, the standard number 0f bootstrap is 4


def bootstrap_linear_model(X,y,block_size,num):
    model_list=[]
    for i in range(num):
        new_X, new_y = bootstrap_con(X, y, block_size)
        model = SVR(kernel='linear', C=0.01, gamma=0.001)
        model.fit(new_X, new_y)
        model_list.append("model/bootstrap_linear_example"+str(i)+".pkl")
        joblib.dump(model,model_list[i])
    return model_list

def bootstrap_GBDT_model(X,y,block_size,num):
    model_list=[]
    for i in range(num):
        new_X, new_y = bootstrap_con(X, y, block_size)
        model = train_gbdt(new_X,new_y)
        model_list.append("model/bootstrap_GBDT_example"+str(i)+".pkl")
        joblib.dump(model,model_list[i])
    return model_list

def EMCM_linear(model,num_bootstrap,model_list,search_times,vector):
    v_list=[]
    for i in range(search_times):
        v=0
        for k in range(num_bootstrap):
            model_e=joblib.load(model_list[k])
            yk=model_e.predict(vector[i].reshape(1, -1))
            fx=model.predict(vector[i].reshape(1, -1))
            v+=np.linalg.norm((fx-yk)*vector[i])
        v_list.append(v)
    temp_list = v_list[:]
    temp_list.sort(reverse=True)
    #top 10 vector in all modified vectors
    vector_list = []
    for i in range(10):
        vector_list.append(vector[v_list.index(temp_list[i])])
    return vector_list


def EMCM_GBDT(model,num_bootstrap,model_list,search_times,vector,num_estimators):
    v_list=[]
    for i in range(search_times):
        v=0
        v_tree = np.zeros(num_estimators)
        for j in range(num_estimators):
            v_tree[j] = model.estimators_[j][0].tree_.predict(vector[i].reshape(1, -1).astype(np.float32))[0]
        for k in range(num_bootstrap):
            model_e=joblib.load(model_list[k])
            yk=model_e.predict(vector[i].reshape(1, -1))
            fx=model.predict(vector[i].reshape(1, -1))
            v+=np.linalg.norm((fx-yk)*v_tree)
        v_list.append(v)
    temp_list = v_list[:]
    temp_list.sort(reverse=True)
    #top 10 vector in all modified vectors
    vector_list = []
    for i in range(10):
        vector_list.append(vector[v_list.index(temp_list[i])])
    return vector_list


if __name__ == '__main__':
    # block_size=int(np.shape(X)[0]**(1/3))+1
    model = joblib.load('model/test.pkl')

    # X_test = np.loadtxt('vector/x.txt')
    # y_test = np.loadtxt('vector/y.txt')

    X_test = np.loadtxt('vector/stage1_batch0.txt')
    y_test = np.loadtxt('vector/LIT101_batch0.txt')
    # block_size=int(np.shape(X_test)[0]**(1/3))+1
    # bootstrap_model(X_test,y_test,block_size,4)
    # a=model.predict(X_test[0].reshape(1, -1))

    vector=[3,2,1]

    print vector.index(max(vector))
