#!/usr/bin/env python2
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
"""Functions and constants to scale current 4-20 mA to measurements, and vice versa.
"""
__all__ = ['P1Flow', 'P1Level','P2Flow', 'P2Cond', 'P2Ph', 'P2Orp','P3Level', 'P3Flow', 'P3DPress' \
		'P4Level', 'P4Hrdss', 'P4Flow', 'P4Orp', \
		'P5FeedPh', 'P5FeedOrp', 'P5FeedCond', 'P5PremCond', 'P5FeedFlow', 'P5PermFlow',\
		'P5ConcFlow', 'P5RecFlow', 'P5HPumpPress', 'P5PermPress', 'P5ConcPress',\
		'P6BackFlow', 'current_to_signal', 'signal_to_current']

#Analog Input AI plc1
class P1Level(object):
    EUMAX = 1225.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0


class P1Flow(object):
    EUMAX = 10.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -15.0

#AI plc2
class P2Flow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -5.0

class P2Cond(object):
    EUMAX = 1000.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P2Ph(object):
    EUMAX = 12.0
    EUMIN = 2.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P2Orp(object):
    EUMAX = 800.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

#AI plc3
class P3Level(object):
    EUMAX = 1250.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P3Flow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -10.0

class P3DPress(object):
    EUMAX = 100.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -18.0

#AI plc4

class P4Level(object):
    EUMAX = 1200.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P4Hrdss(object):
    EUMAX = 150.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P4Flow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -5.0

class P4Orp(object):
    EUMAX = 800.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

#AI plc5

class P5FeedPh(object):
    EUMAX = 12.0
    EUMIN = 2.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P5FeedOrp(object):
    EUMAX = 800.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P5FeedCond(object):
    EUMAX = 1000.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P5PremCond(object):
    EUMAX = 1300.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P5FeedFlow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 5.0

class P5PermFlow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -15.0

class P5ConcFlow(object):
    EUMAX = 4.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -30.0

class P5RecFlow(object):
    EUMAX = 2.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -10.0

class P5HPumpPress(object):
    EUMAX = 500.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

class P5PermPress(object):
    EUMAX = 500.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -5.0

class P5ConcPress(object):
    EUMAX = 500.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = 0.0

#AI plc6
class P6BackFlow(object):
    EUMAX = 2.0
    EUMIN = 0.0
    RAWMAX = 31208.0
    RAWMIN = -5.0


def current_to_signal(raw_in, scaling):
    """
    Scales the input signal from current 4 - 20 mA to the human readable measurements.
    :param raw_in: current value.
    :param scaling: scaling constants.
    :return: signal value.
    """
    if raw_in > scaling.RAWMAX:
        return 0.0
    result = raw_in - scaling.RAWMIN
    result *= (scaling.EUMAX - scaling.EUMIN) / (scaling.RAWMAX - scaling.RAWMIN)
    result += scaling.EUMIN
    return result



def signal_to_current(scale_in, scaling):
    """
    Scales the input signal from human readable measurements to current 4 - 20 mA.
    :param scale_in: signal value.
    :param scaling: scaling constants.
    :return: current value.
    """
    result = scale_in - scaling.EUMIN
    result /= (scaling.EUMAX - scaling.EUMIN) / (scaling.RAWMAX - scaling.RAWMIN)
    result += scaling.RAWMIN
    return 0 if result < 0 else result


