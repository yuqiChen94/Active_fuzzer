#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *
import pandas as pd
import numpy as np
import time
from bitdump import *
def map_ip_address(nstage):
    return {
        1: "192.168.0.1",
        2: "192.168.0.2",
        3: "192.168.0.3",
        4: "192.168.0.4"
    }.get(nstage, "error")

def extract_bits(date,nstage,sensor,num):
    stage='stage'+str(nstage)
    pkts = PcapReader('packet/' + date + stage + '.pcap')
    files = pd.read_csv('log/' + date + sensor + '.csv')
    start_time = files[" Timestamp"][1]
    # start_time = ' 1/8/2019 9:30:43 PM'
    print start_time
    a = time.strptime(start_time, ' %d/%m/%Y %I:%M:%S %p')
    t0 = time.mktime(a)
    ip1=map_ip_address(nstage)+'2'
    ip2=map_ip_address(nstage)+'0'
    count = 1
    second_count = 0
    templist = []
    p2_50 = np.zeros(256, dtype=int)
    p2_40 = np.zeros(176, dtype=int)
    p2_28 = np.zeros(80, dtype=int)
    p0_40 = np.zeros(176, dtype=int)

    while True:
        pkt = pkts.read_packet()
        if pkt is None:
            break
        else:
            # print pkt.time
            if pkt.time < Decimal(t0):
                continue
            if pkt.haslayer("Raw"):
                if pkt["IP"].src == ip1:
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
                if pkt["IP"].src == ip2:
                    if len(pkt[Raw]) == 22:
                        a = bitdump(pkt[Raw])
                        for j in range(len(a)):
                            p0_40[j] = a[j]
            if pkt.time - Decimal(t0) >= 1:
                temp = np.hstack((p2_50, p2_40, p2_28, p0_40))
                templist.append(temp)
                t0 = pkt.time
                print(count)
                count += 1


            if count>num:
                break

    x = np.array(templist)

    # print x
    # print len(x[0])
    q = time.time()
    # np.save('vector/'+date+stage+'_whole.npy', x)
    print time.time() - q
    np.save('vector/'+date+stage+'_whole.npy', x)
    pkts.close()

    return 0
date = '0806'
nstage=4
sensor = 'LIT401'

extract_bits(date,nstage,sensor,1000)
