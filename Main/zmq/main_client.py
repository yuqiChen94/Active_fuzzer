#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import zmq
import numpy as np


def save(filename, contents):
	fh = open(filename, 'w')
	fh.write(contents)
	fh.close()


ip1 = "10.0.1.231"
ip2 = "10.0.1.232"
ip3 = "10.0.1.233"
ip4 = "10.0.1.234"
port_vector = "5510"
port_pv = '5511'
port_capture = '5512'
#  Socket to talk to server
tcp_address1 = "tcp://" + ip1 + ":" + port_vector
tcp_address2 = "tcp://" + ip2 + ":" + port_vector
tcp_address3 = "tcp://" + ip3 + ":" + port_vector
tcp_address4 = "tcp://" + ip4 + ":" + port_vector
tcp_address1_pv = "tcp://" + ip1 + ":" + port_pv
tcp_address2_pv = "tcp://" + ip2 + ":" + port_pv
tcp_address3_pv = "tcp://" + ip3 + ":" + port_pv
tcp_address4_pv = "tcp://" + ip4 + ":" + port_pv
tcp_address1_capture = "tcp://" + ip1 + ":" + port_capture
tcp_address2_capture = "tcp://" + ip2 + ":" + port_capture
tcp_address3_capture = "tcp://" + ip3 + ":" + port_capture
tcp_address4_capture = "tcp://" + ip4 + ":" + port_capture

context = zmq.Context()
socket1 = context.socket(zmq.SUB)
socket1.connect(tcp_address1)
socket2 = context.socket(zmq.SUB)
socket2.connect(tcp_address2)
socket3 = context.socket(zmq.SUB)
socket3.connect(tcp_address3)
socket4 = context.socket(zmq.SUB)
socket4.connect(tcp_address4)
socket1_pv = context.socket(zmq.SUB)
socket1_pv.connect(tcp_address1_pv)
socket2_pv = context.socket(zmq.SUB)
socket2_pv.connect(tcp_address2_pv)
socket3_pv = context.socket(zmq.SUB)
socket3_pv.connect(tcp_address3_pv)
socket4_pv = context.socket(zmq.SUB)
socket4_pv.connect(tcp_address4_pv)
socket1_capture = context.socket(zmq.SUB)
socket1_capture.connect(tcp_address1_capture)
socket2_capture = context.socket(zmq.SUB)
socket2_capture.connect(tcp_address2_capture)
socket3_capture = context.socket(zmq.SUB)
socket3_capture.connect(tcp_address3_capture)
socket4_capture = context.socket(zmq.SUB)
socket4_capture.connect(tcp_address4_capture)
socket1.setsockopt(zmq.SUBSCRIBE, '')
socket2.setsockopt(zmq.SUBSCRIBE, '')
socket3.setsockopt(zmq.SUBSCRIBE, '')
socket4.setsockopt(zmq.SUBSCRIBE, '')
socket1_pv.setsockopt(zmq.SUBSCRIBE, '')
socket2_pv.setsockopt(zmq.SUBSCRIBE, '')
socket3_pv.setsockopt(zmq.SUBSCRIBE, '')
socket4_pv.setsockopt(zmq.SUBSCRIBE, '')
socket1_capture.setsockopt(zmq.SUBSCRIBE, '')
socket2_capture.setsockopt(zmq.SUBSCRIBE, '')
socket3_capture.setsockopt(zmq.SUBSCRIBE, '')
socket4_capture.setsockopt(zmq.SUBSCRIBE, '')
capture_flag = 'False'
save('capture_flag1.txt', capture_flag)
save('capture_flag2.txt', capture_flag)
save('capture_flag3.txt', capture_flag)
save('capture_flag4.txt', capture_flag)


def preprocess_message(x):
	temp = x.strip('[')
	temp = temp
	final = np.fromstring(temp, dtype=int, sep=', ')
	return final


while True:
	capture_flag1 = socket1_capture.recv_string()
	s1old = socket1.recv()
	s1old = preprocess_message(s1old)
	print s1old
	pv1 = socket1_pv.recv_string()
	capture_flag2 = socket2_capture.recv()
	s2old = socket2.recv()
	s2old = preprocess_message(s2old)
	capture_flag3 = socket3_capture.recv()
	s3old = socket3.recv()
	s3old = preprocess_message(s3old)
	capture_flag4 = socket4_capture.recv()
	s4old = socket4.recv()
	s4old = preprocess_message(s4old)
	save('capture_flag1.txt', capture_flag1)
	save('capture_flag2.txt', capture_flag2)
	save('capture_flag3.txt', capture_flag3)
	save('capture_flag4.txt', capture_flag4)
	np.savetxt('stage1old.txt', s1old,fmt='%d')
	np.savetxt('stage2old.txt', s2old,fmt='%d')
	np.savetxt('stage3old.txt', s3old,fmt='%d')
	np.savetxt('stage4old.txt', s4old,fmt='%d')
	save('pv1.txt', pv1)
