# -*- coding: utf-8 -*-
"""
Created on Sunday Dec 24 21:53:00 2017
@author: Yangpei
"""

import tushare as ts


def get_1min_tick(code, cons):
    """
    此API  ts.bar只能获得100天内的数据
    :param code:
    :param cons:
    :return:
    """
    return ts.bar(code, conn=cons, freq='1min', start_date='2014-01-01', end_date='',
                  ma=[5, 13, 21, 34, 55, 89, 144, 233],
                  factors=['vr', 'tor'])
