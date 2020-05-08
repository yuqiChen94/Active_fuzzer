#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import zmq
import time
import numpy as np


def preprocess(x):
	temp = x.strip('[')
	temp = temp.strip(']')
	final = np.fromstring(temp, dtype=int, sep='. ')
	return final


def save(filename, contents):
	fh = open(filename, 'w')
	fh.write(contents)
	fh.close()


def read(filename):
	fh = open(filename, 'r')
	contents = fh.read()
	fh.close()
	return contents


ip = "10.0.1.235"
port = "5503"
port_states = '5507'
tcp_address = "tcp://" + ip + ":" + port
tcp_address_states = "tcp://" + ip + ":" + port_states

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(tcp_address)
socket.setsockopt(zmq.SUBSCRIBE, '')
socket_states = context.socket(zmq.SUB)
socket_states.connect(tcp_address_states)
socket_states.setsockopt(zmq.SUBSCRIBE, '')

while True:
	newvector = socket.recv_string()
	print newvector
	newvector = preprocess(newvector)
	np.savetxt('newvector.txt',newvector)
	states = socket_states.recv_string()
	save('stage_states.txt',states)
