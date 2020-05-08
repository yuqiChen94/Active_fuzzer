#!/usr/bin/env python
# -*- coding:utf-8 -*-
import zmq
import time
import numpy as np


def save(filename, contents):
	fh = open(filename, 'w')
	fh.write(contents)
	fh.close()


def read(filename):
	fh = open(filename, 'r')
	contents = fh.read()
	fh.close()
	return contents


'''set tcp address'''
ip = "10.0.1.233"
port_vector = "5510"
tcp_address_vector = "tcp://" + ip + ":" + port_vector
port_pv = "5511"
tcp_address_pv = "tcp://" + ip + ":" + port_pv
port_capture = "5512"
tcp_address_capture = "tcp://" + ip + ":" + port_capture

context = zmq.Context()
socket_vector = context.socket(zmq.PUB)
socket_vector.bind(tcp_address_vector)
socket_pv = context.socket(zmq.PUB)
socket_pv.bind(tcp_address_pv)
socket_capture = context.socket(zmq.PUB)
socket_capture.bind(tcp_address_capture)
capture_flag = 'False'
pv_diff = '0'
stageold = [0]


while True:
	'''send old vector to laptop'''
	capture_flag = read('capture_flag1.txt')
	socket_capture.send_string(capture_flag)
	vo = map(int,np.loadtxt('stage1old.txt').tolist())
	socket_vector.send_string(str(vo))
	pv_diff = read('pv_diff.txt')
	socket_pv.send_string(str(pv_diff))
	time.sleep(1)
