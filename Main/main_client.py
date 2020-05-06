#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import zmq
import numpy as np

ip1 = "10.0.1.231"
ip2 = "10.0.1.232"
ip3 = "10.0.1.233"
ip4 = "10.0.1.234"
port = "5510"

tcp_address1 = "tcp://" + ip1 + ":" + port
tcp_address2 = "tcp://" + ip2 + ":" + port
tcp_address3 = "tcp://" + ip3 + ":" + port
tcp_address4 = "tcp://" + ip4 + ":" + port
#  Socket to talk to server
context = zmq.Context()
socket1 = context.socket(zmq.SUB)
socket1.connect(tcp_address1)
socket2 = context.socket(zmq.SUB)
socket2.connect(tcp_address2)
socket3 = context.socket(zmq.SUB)
socket3.connect(tcp_address3)
socket4 = context.socket(zmq.SUB)
socket4.connect(tcp_address4)


socket1.setsockopt(zmq.SUBSCRIBE, '')
socket2.setsockopt(zmq.SUBSCRIBE, '')
socket3.setsockopt(zmq.SUBSCRIBE, '')
socket4.setsockopt(zmq.SUBSCRIBE, '')

def preprocess(x):
    temp = x.strip('[')
    temp = temp.strip(']')
    final = np.fromstring(temp, dtype=int, sep='. ')
    return final


while True:
    vnold1 = socket1.recv_string()
    old1 = preprocess(vnold1)
    # vnold2 = socket2.recv_string()
    # old2 = preprocess(vnold2)
    # vnold3 = socket3.recv_string()
    # old3 = preprocess(vnold3)
    # oldvector = np.hstack((old1, old2, old3))
    # np.savetxt("oldvector.txt", oldvector)
    np.savetxt('stage1old.txt',old1)
