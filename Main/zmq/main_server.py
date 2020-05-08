import zmq
import numpy as np
import time


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
ip = "10.0.1.235"
port1 = "5501"
port2 = "5502"
port3 = "5503"
port4 = "5504"
port1_states = "5505"
port2_states = "5506"
port3_states = "5507"
port4_states = "5508"
tcp_address1 = "tcp://" + ip + ":" + port1
tcp_address2 = "tcp://" + ip + ":" + port2
tcp_address3 = "tcp://" + ip + ":" + port3
tcp_address4 = "tcp://" + ip + ":" + port4
tcp_address1_states = "tcp://" + ip + ":" + port1_states
tcp_address2_states = "tcp://" + ip + ":" + port2_states
tcp_address3_states = "tcp://" + ip + ":" + port3_states
tcp_address4_states = "tcp://" + ip + ":" + port4_states


context = zmq.Context()
socket1 = context.socket(zmq.PUB)
socket1.bind(tcp_address1)
socket2 = context.socket(zmq.PUB)
socket2.bind(tcp_address2)
socket3 = context.socket(zmq.PUB)
socket3.bind(tcp_address3)
socket4 = context.socket(zmq.PUB)
socket4.bind(tcp_address4)
socket1_states = context.socket(zmq.PUB)
socket1_states.bind(tcp_address1_states)
socket2_states = context.socket(zmq.PUB)
socket2_states.bind(tcp_address2_states)
socket3_states = context.socket(zmq.PUB)
socket3_states.bind(tcp_address3_states)
socket4_states = context.socket(zmq.PUB)
socket4_states.bind(tcp_address4_states)
'''
np.savetxt('newvector.txt',[1,0])
save('stage_states.txt', '0 0')
'''

while True:
	'''send new vector and stage states to different stages'''
	index = np.loadtxt('newvector.txt')
	stage_states = read('stage_states.txt')
	socket1.send_string("%s" % index)
	socket1_states.send_string(stage_states)
	socket2.send_string("%s" % index)
	socket2_states.send_string(stage_states)
	socket3.send_string("%s" % index)
	socket3_states.send_string(stage_states)
	socket4.send_string("%s" % index)
	socket4_states.send_string(stage_states)
	time.sleep(1)
