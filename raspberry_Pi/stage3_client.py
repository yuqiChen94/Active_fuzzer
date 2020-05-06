#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
import zmq
import numpy as np

ip = "10.0.1.235"
port = "5503"

tcp_address = "tcp://" + ip + ":" + port

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(tcp_address)


socket.setsockopt(zmq.SUBSCRIBE, '')


def preprocess(x):
    temp = x.strip('[')
    temp = temp.strip(']')
    final = np.fromstring(temp,dtype=int,sep='. ')
    return final


while True:
    vnew = socket.recv_string()
    new = preprocess(vnew)
    np.savetxt('stage3new.txt',new)
