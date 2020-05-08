from scapy.all import *
import time
import numpy as np
from bitdump import *
import binascii
from netfilterqueue import NetfilterQueue
from usl import *
import _PLC1


def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()


t = time.time()
time_interval = 30
pv_list = np.zeros(100,dtype=float)
pv_list = pv_list.tolist()
count = 0
while True:
    if time.time() - t <= 1:
        continue
    else:
        f = open('string.txt','r')
        line = f.readline()
        pkt = IP(binascii.unhexlify(line))
        if pkt.haslayer('SWAT_P1_RIO_AI'):
            pv = usl(pkt['SWAT_P1_RIO_AI'].level)
            pv_list[count] = pv
            print pv_list
            diff = pv_list[count]-pv_list[count-time_interval]
            count += 1
            if count == 100:
                count = 0
            t = time.time()
            save('zmq/pv_diff1.txt', str(diff))
