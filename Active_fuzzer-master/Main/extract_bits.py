#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *
import pandas as pd
import numpy as np
import time

from bitdump import *

index12_50 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 97, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 186, 187, 188, 189, 190, 191, 192, 193, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 221, 222, 223, 224, 225, 239, 240, 241, 253, 254, 255, 256, 257, 269, 270, 271, 272, 273, 302, 303, 304, 305, 318, 319, 320, 321, 334, 335, 336, 337, 350, 351, 352, 353, 367, 368, 369, 384]
index12_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97]
index12_28 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97, 142, 143, 144, 145, 190, 200, 201]
index10_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 95, 96, 97, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 206, 207, 209, 217]
# print len(index12_50)
# print len(index12_40)
# print len(index12_28)
# print len(index10_40)
# print len(index12_50)+len(index12_40)+len(index12_28)+len(index10_40)
p12_50 = np.zeros(len(index12_50),dtype=int)
p12_40 = np.zeros(len(index12_40),dtype=int)
p12_28 = np.zeros(len(index12_28),dtype=int)
p10_40 = np.zeros(len(index10_40),dtype=int)

pkts = PcapReader("packet/0712stage1_b.pcap")
file = pd.read_csv("log/0712LIT301b.csv")
start_time = file[" Timestamp"][1]
a = time.strptime(start_time,' %d/%m/%Y %I:%M:%S %p')
t0 = time.mktime(a)
count = 1
templist = []
while True:
    pkt = pkts.read_packet()
    if pkt is None:
        break
    else:
        if (int(pkt.time) < t0):
            continue
        else:
            if (pkt.haslayer("Raw")):
                if (pkt["IP"].src == '192.168.0.12'):
                    if (len(pkt[Raw]) == 50):
                        a = bitdump(pkt[Raw])
                        for i in range(len(index12_50)):
                            p12_50[i] = a[index12_50[i]]
                    if (len(pkt[Raw]) == 40):
                        a = bitdump(pkt[Raw])
                        for i in range(len(index12_40)):
                            p12_40[i] = a[index12_40[i]]
                    if (len(pkt[Raw]) == 28):
                        a = bitdump(pkt[Raw])
                        for i in range(len(index12_28)):
                            p12_28[i] = a[index12_28[i]]
                if (pkt["IP"].src == '192.168.0.10'):
                    if (len(pkt[Raw]) == 40):
                        a = bitdump(pkt[Raw])
                        for i in range(len(index10_40)):
                            p10_40[i] = a[index10_40[i]]
            if (pkt.time - t0 >= 1):
                t0 = pkt.time
                print(count)
                temp = np.hstack((p12_50,p12_40,p12_28,p10_40))
                templist.append(temp)
                count += 1

x = np.array(templist)
np.savetxt('vector/0712stage1b_bitsnew.txt',x,fmt="%d")
pkts.close()


