#!/usr/bin/python
# -*- coding: utf8 -*-
# cp936

#===============================================================================
# 作者：fasiondog
# 历史：1）20130419, Added by fasiondog
#===============================================================================

from ._trade_sys import *
from hikyuu.util.unicode import (unicodeFunc, reprFunc)

SignalBase.__unicode__ = unicodeFunc
SignalBase.__repr__ = reprFunc

SG_Flex.__doc__ = SG_Flex.__doc__ + """\n
使用指标的EMA平滑值作为慢线，但指标上穿慢线时买入，指标下穿慢线时卖出。
参数：
    n：慢线EMA参数
"""