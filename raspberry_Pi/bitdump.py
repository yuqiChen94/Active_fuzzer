#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *

def bitdump(x, dump=False):
    s = ""
    x = raw(x)
    l = len(x)
    i = 0
    while i < l:
        for j in range(16):
            if i+j < l:
                s += "%02X" % orb(x[i+j])
                s+=""
            if j%16 == 7:
                s += ""
        i += 16
    if s.endswith("\n"):
        s = s[:-1]
    return bin(int(s,16)).replace("0b","")