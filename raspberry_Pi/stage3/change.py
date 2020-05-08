#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scapy.all import *
import random
import time
import numpy as np
#from bitdump import *
import binascii
import CIP_sequence
#from modify_bit import *
from netfilterqueue import NetfilterQueue
import zmq
from AL_utils import *


p2_50 = np.zeros(394, dtype=int)
p2_40 = np.zeros(314, dtype=int)
p2_28 = np.zeros(218, dtype=int)
p0_40 = np.zeros(314, dtype=int)
total_length = len(p2_50)+len(p2_40)+len(p2_28)+len(p0_40)
vector = np.hstack((p2_50,p2_40,p2_28,p0_40))
vector = vector.tolist()
modify_time = 0
modify_flag = 1
accept_flag = 0
capture_flag = 'False'
count = 0
start_time = 0
check_time = 0
time_interval = 30
new_vector = np.loadtxt('newvector.txt')
new_vector = new_vector.tolist()
new_vector[581] = 0
new_vector[583] = 0
print new_vector[581],new_vector[583]
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
    if modify_flag == 1:
        start_time = time.time()
        if pkt.haslayer('Raw'):
            if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 32:
                rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,1))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['IP'].len
                del pktnew['UDP'].chksum
                del pktnew['UDP'].len
                packet.set_payload(str(pktnew))
            if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 22:
                rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,2))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['IP'].len
                del pktnew['UDP'].chksum
                del pktnew['UDP'].len
                packet.set_payload(str(pktnew))
            if pkt['IP'].src == '192.168.0.12' and len(pkt['Raw']) == 10:
                rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,3))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['IP'].len
                del pktnew['UDP'].chksum
                del pktnew['UDP'].len
                packet.set_payload(str(pktnew))
            if pkt['IP'].src == '192.168.0.10' and len(pkt['Raw']) == 22:
                a = time.time()
                rawpkt = binascii.unhexlify(reconstruct_packet(pkt,new_vector,1,4))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['IP'].len
                del pktnew['UDP'].chksum
                del pktnew['UDP'].len
                packet.set_payload(str(pktnew))
                print time.time()-a
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
        print "[*] stopping NFQUEUE"
        nfqueue.unbind()
