#!/usr/bin/env python
# -*- coding:utf-8 -*-
import zmq
import numpy as np
import time

'''set tcp address'''
ip = "10.0.1.232"
port = "5510"
tcp_address = "tcp://" + ip + ":" + port


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(tcp_address)


while True:
    '''send old vector to laptop'''
    vo = np.loadtxt('stage2old.txt')
    socket.send_string("%s" % vo)
    time.sleep(1)