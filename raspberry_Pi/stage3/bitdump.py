#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from scapy.all import *
import binascii


def hex_to_bin(hex_string):
    hex_list = list(hex_string)
    bin_list = []
    for i in range(len(hex_list)):
        if hex_list[i] == '0':
            bin_list.extend(['0','0','0','0'])
        if hex_list[i] == '1':
            bin_list.extend(['0','0','0','1'])
        if hex_list[i] == '2':
            bin_list.extend(['0','0','1','0'])
        if hex_list[i] == '3':
            bin_list.extend(['0','0','1','1'])
        if hex_list[i] == '4':
            bin_list.extend(['0','1','0','0'])
        if hex_list[i] == '5':
            bin_list.extend(['0','1','0','1'])
        if hex_list[i] == '6':
            bin_list.extend(['0','1','1','0'])
        if hex_list[i] == '7':
            bin_list.extend(['0','1','1','1'])
        if hex_list[i] == '8':
            bin_list.extend(['1','0','0','0'])
        if hex_list[i] == '9':
            bin_list.extend(['1','0','0','1'])
        if hex_list[i] == 'a':
            bin_list.extend(['1','0','1','0'])
        if hex_list[i] == 'b':
            bin_list.extend(['1','0','1','1'])
        if hex_list[i] == 'c':
            bin_list.extend(['1','1','0','0'])
        if hex_list[i] == 'd':
            bin_list.extend(['1','1','0','1'])
        if hex_list[i] == 'e':
            bin_list.extend(['1','1','1','0'])
        if hex_list[i] == 'f':
            bin_list.extend(['1','1','1','1'])
    bin_str = ''.join(bin_list)
    return bin_str


def bitdump(x, dump=False):
    hex_string = binascii.hexlify(bytes(x))
    bin_string = hex_to_bin(hex_string)
    return list(map(int,list(bin_string)))