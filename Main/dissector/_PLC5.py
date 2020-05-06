# -*- coding: utf-8 -*-
# Copyright (c) 2018 Beebi Siti Salimah Binte Liyakkathali, liyakkathali@sutd.edu.sg
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from scapy import all as scapy_all
import enip_cpf

__all__ = ['SWAT_P5_RIO_DO', 'SWAT_P5_RIO_DI', 'SWAT_P5_RIO_AI']

class SWAT_P5_RIO_DO(scapy_all.Packet):
    name = "SWAT_P5_RIO_DO"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.ByteField('number', 0),
        scapy_all.StrFixedLenField('reserved', 0, length=5),
       
        scapy_all.BitEnumField('MV504_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV504_Open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV503_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV503_Open', 0, 1, {0: 'disable', 1: 'enable'}),
	    scapy_all.BitEnumField('MV502_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV502_Open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV501_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV501_Open', 0, 1, {0: 'disable', 1: 'enable'}),
	   
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        
    
    ]

class SWAT_P5_RIO_DI(scapy_all.Packet):
    name = 'SWAT_P5_RIO_DI'
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        
        scapy_all.BitEnumField('P502_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P502_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P502_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P501_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P501_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P501_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('RIO5_Wifi', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('PLC5_Wifi', 0, 1, {0: 'disable', 1: 'enable'}),
	    
        scapy_all.BitEnumField('MV504_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV504_Open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV503_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV503_Open', 0, 1, {0: 'disable', 1: 'enable'}),
	    scapy_all.BitEnumField('MV502_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV502_Open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV501_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV501_Open', 0, 1, {0: 'disable', 1: 'enable'}),
	   
	    scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        #scapy_all.BitEnumField('VSD502_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        #scapy_all.BitEnumField('VSD501_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.LEShortField('VSD502_Start', 0),          #VSD is pump
        scapy_all.LEShortField('VSD501_Start', 0),

        scapy_all.BitEnumField('PSH501_High', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('PSL501_Low', 0, 1, {0: 'disable', 1: 'enable'}),
        
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
       
 ]


class SWAT_P5_RIO_AI(scapy_all.Packet):
    name = "SWAT_P5_RIO_AI"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        scapy_all.LEShortField('AIT501_pH', 0),
        scapy_all.LEShortField('AIT502_ORP', 0),
        scapy_all.LEShortField('AIT503_Water_Cond', 0),
        scapy_all.LEShortField('AIT504_Perm_Cond', 0),
        scapy_all.LEShortField('FIT501_Feed_Flow', 0),
        scapy_all.LEShortField('FIT502_Perm_Flow', 0),
        scapy_all.LEShortField('FIT503_Con_Flow', 0),
        scapy_all.LEShortField('FIT504_Recirculation_Flow', 0),
        scapy_all.LEShortField('PIT501_RO_Pressure', 0),
        scapy_all.LEShortField('PIT502_Perm_Pressure', 0),
        scapy_all.LEShortField('PIT503_Con_Pressure', 0),
        scapy_all.LEShortField('spare', 0),
      
    ]

scapy_all.bind_layers(scapy_all.TCP, enip_cpf.ENIP_CPF, dport=2222)
scapy_all.bind_layers(scapy_all.UDP, enip_cpf.ENIP_CPF, sport=2222)

scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P5_RIO_AI, length=32)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P5_RIO_DI, length=10)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P5_RIO_DO, length=22)

