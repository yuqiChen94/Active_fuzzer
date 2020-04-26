#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
import binascii
from scapy.all import *
import string

def flip(pkt1,number):
    flag = 0
    whole = binascii.hexlify(bytes(pkt1))
    payload = binascii.hexlify(bytes(pkt1[Raw]))
    temp = string.replace(whole,payload,"")
    templist = list(payload)
    if templist[0] == '0':
        flag = 1
    a = bin(int(payload,16))
    a = string.replace(a,"0b","")
    b = list(a)
    if b[number] == '1':
        b[number] = '0'
    else:
        b[number] = '1'
    c = ''.join(b)
    d = hex(int(c,2))
    payloadnew = string.replace(d,"0x","")
    payloadnew = string.replace(payloadnew,"L","")
    if flag == 1:
        payloadnew = list(payloadnew)
        payloadnew.insert(0,'0')
        payloadnew = ''.join(payloadnew)
    packetnew = temp + payloadnew
    return packetnew


def on(pkt1,number):
	flag = 0
	whole = binascii.hexlify(bytes(pkt1))
	payload = binascii.hexlify(bytes(pkt1[Raw]))
	temp = string.replace(whole,payload,"")
	templist = list(payload)
	if templist[0] == '0':
		flag = 1
	a = bin(int(payload,16))
	a = string.replace(a,"0b","")
	b = list(a)
	b[number] = '1'
	c = ''.join(b)
	d = hex(int(c,2))
	payloadnew = string.replace(d,"0x","")
	payloadnew = string.replace(payloadnew,"L","")
	if flag == 1:
		payloadnew = list(payloadnew)
		payloadnew.insert(0,'0')
		payloadnew = ''.join(payloadnew)
	packetnew = temp + payloadnew
	return packetnew


def off(pkt1,number):
	flag = 0
	whole = binascii.hexlify(bytes(pkt1))
	payload = binascii.hexlify(bytes(pkt1[Raw]))
	temp = string.replace(whole,payload,"")
	templist = list(payload)
	if templist[0] == '0':
		flag = 1
	a = bin(int(payload,16))
	a = string.replace(a,"0b","")
	b = list(a)
	b[number] = '0'
	c = ''.join(b)
	d = hex(int(c,2))
	payloadnew = string.replace(d,"0x","")
	payloadnew = string.replace(payloadnew,"L","")
	if flag == 1:
		payloadnew = list(payloadnew)
		payloadnew.insert(0,'0')
		payloadnew = ''.join(payloadnew)
	packetnew = temp + payloadnew
	return packetnew


