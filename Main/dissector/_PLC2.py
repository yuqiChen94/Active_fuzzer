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

__all__ = ['SWAT_P2_RIO_DO', 'SWAT_P2_RIO_DI', 'SWAT_P2_RIO_AI']

class SWAT_P2_RIO_DI(scapy_all.Packet):
    name = "SWAT_P2_RIO_DI" 
    fields_desc =[
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),


        scapy_all.BitEnumField('P202_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P202_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P202_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P201_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P201_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P201_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('RIO2_Wifi', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('PLC2_Wifi', 0, 1, {0: 'disable', 1: 'enable'}),

        scapy_all.BitEnumField('P205_Run', 0, 1, {0: 'disable', 1: 'enable'}),
		scapy_all.BitEnumField('P205_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P204_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P204_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P204_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P203_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P203_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P203_Auto', 0, 1, {0: 'disable', 1: 'enable'}),

		scapy_all.BitEnumField('P208_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P207_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
    	scapy_all.BitEnumField('P207_Run', 0, 1, {0: 'disable', 1: 'enable'}),
		scapy_all.BitEnumField('P207_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P206_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P206_Run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P206_Auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P205_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
        
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('LS203_Low', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('LS202_Low', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('LS201_Low', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV201_Close', 0, 1, {0: 'disable', 1: 'enable'}), 
        scapy_all.BitEnumField('MV201_Open', 0, 1, {0: 'disable', 1: 'enable'}),  
        scapy_all.BitEnumField('P208_Fault', 0, 1, {0: 'disable', 1: 'enable'}),
    	scapy_all.BitEnumField('P208_Run', 0, 1, {0: 'disable', 1: 'enable'}),
       
    ]

class SWAT_P2_RIO_DO(scapy_all.Packet):
    name = "SWAT_P2_RIO_DO"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.ByteField('number', 0),
        scapy_all.StrFixedLenField('reserved', 0, length=5),
       
        scapy_all.BitEnumField('P208_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P207_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P206_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P205_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P204_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P203_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P202_Start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('P201_Start', 0, 1, {0: 'disable', 1: 'enable'}),
	   
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('spare', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('LED_RED', 0, 1, {0: 'disable', 1: 'enable'}),  #LED_RED
        scapy_all.BitEnumField('MV201_Close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('MV201_Open', 0, 1, {0: 'disable', 1: 'enable'}),
        
    ]

class SWAT_P2_RIO_AI(scapy_all.Packet):
    name = "SWAT_P2_RIO_AI"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        scapy_all.LEShortField('FIT201_Flow', 0),
        scapy_all.LEShortField('AIT201_Conductivity', 0),
        scapy_all.LEShortField('AIT202_pH', 0),
        scapy_all.LEShortField('AIT203_ORP', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
        scapy_all.LEShortField('spare', 0),
      
    ]

scapy_all.bind_layers(scapy_all.TCP, enip_cpf.ENIP_CPF, dport=2222)
scapy_all.bind_layers(scapy_all.UDP, enip_cpf.ENIP_CPF, sport=2222)

scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P2_RIO_AI, length=32)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P2_RIO_DI, length=10)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P2_RIO_DO, length=22)
