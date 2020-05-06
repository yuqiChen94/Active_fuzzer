import zmq
import numpy as np
import time

'''set tcp address'''
ip = "10.0.1.235"
port1 = "5501"
port2 = "5502"
port3 = "5503"
port4 = "5504"
tcp_address1 = "tcp://" + ip + ":" + port1
tcp_address2 = "tcp://" + ip + ":" + port2
tcp_address3 = "tcp://" + ip + ":" + port3
tcp_address4 = "tcp://" + ip + ":" + port4

context = zmq.Context()
socket1 = context.socket(zmq.PUB)
socket1.bind(tcp_address1)
socket2 = context.socket(zmq.PUB)
socket2.bind(tcp_address2)
socket3 = context.socket(zmq.PUB)
socket3.bind(tcp_address3)
socket4 = context.socket(zmq.PUB)
socket4.bind(tcp_address4)


while True:
    '''send new vector to different stages'''
    vn1 = np.loadtxt('stage1new.txt')
    vn2 = np.loadtxt('stage2new.txt')
    vn3 = np.loadtxt('stage3new.txt')
    vn4 = np.loadtxt('stage4new.txt')
    socket1.send_string("%s" % vn1)
    socket2.send_string("%s" % vn2)
    socket3.send_string("%s" % vn3)
    socket4.send_string("%s" % vn4)
    time.sleep(1)
