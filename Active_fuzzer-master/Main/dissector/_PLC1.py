# -*- coding: utf-8 -*-
# Copyright (c) 2015 David I. Urbina, david.urbina@utdallas.edu
#
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
"""Scapy Dissector for Ethernet/IP Implicit I/O messages of PLC 1."""
from scapy import all as scapy_all

import enip_cpf

__all__ = ['SWAT_P1_PLC', 'SWAT_P1_RIO_DO', 'SWAT_P1_RIO_DI', 'SWAT_P1_RIO_AI', 'SWAT_P1_WRIO_AI']


class SWAT_P1_PLC(scapy_all.Packet):
    name = "SWAT_P1_PLC"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('number', 0),
        scapy_all.LEShortField('spare', 0),
    ]


class SWAT_P1_RIO_DO(scapy_all.Packet):
    name = "SWAT_P1_RIO_DO"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.ByteField('number', 0),
        scapy_all.StrFixedLenField('reserved', 0, length=5),
        scapy_all.BitField('spare', 0, 4),
        scapy_all.BitEnumField('valve_close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('valve_open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump2_start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump1_start', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.FieldListField("spare2", [], scapy_all.ByteField('', 0),
                                 length_from=lambda p: p.underlayer.length - 9),
    ]


class SWAT_P1_RIO_DI(scapy_all.Packet):
    name = 'SWAT_P1_RIO_DI'
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        scapy_all.BitEnumField('pump2_fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump2_run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump2_auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump1_fault', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump1_run', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('pump1_auto', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('rio_wireless', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('plc_wireless', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitField('spare', 0, 6),
        scapy_all.BitEnumField('valve_close', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.BitEnumField('valve_open', 0, 1, {0: 'disable', 1: 'enable'}),
        scapy_all.LEShortField('spare2', 0),
    ]


class SWAT_P1_RIO_AI(scapy_all.Packet):
    name = "SWAT_P1_RIO_AI"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        scapy_all.LEShortField('level', 0),
        scapy_all.LEShortField('flow', 0),
        scapy_all.FieldListField("spare", [], scapy_all.LEShortField("", 0),
                                 length_from=lambda p: p.underlayer.length - 10),
    ]


class SWAT_P1_WRIO_AI(scapy_all.Packet):
    name = "SWAT_P1_WRIO_AI"
    fields_desc = [
        scapy_all.LEShortField('counter', 0),
        scapy_all.LEIntField('padding', 0),
        scapy_all.LEShortField('level', 0),
        scapy_all.LEShortField('flow', 0),
        scapy_all.FieldListField("spare", [], scapy_all.LEShortField("", 0),
                                 length_from=lambda p: p.underlayer.length - 10),
    ]


scapy_all.bind_layers(scapy_all.TCP, enip_cpf.ENIP_CPF, dport=2222)
scapy_all.bind_layers(scapy_all.UDP, enip_cpf.ENIP_CPF, sport=2222)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P1_RIO_AI, length=32)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P1_RIO_DI, length=10)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P1_RIO_DO, length=22)
scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P1_PLC, length=8)  # Comment for WRIO
# scapy_all.bind_layers(enip_cpf.CPF_AddressDataItem, SWAT_P1_WRIO_AI, length=10)  # Uncomment for WRIO
