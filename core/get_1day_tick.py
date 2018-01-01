import tushare as ts


def get_1day_tick(code):
    """
    一次性获得该股票所有的日线数据: [open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover]
    :param code:
    :return:
    """
    return ts.get_hist_data(code)


def get_1day_tick(code, start, end):
    """
    通过日期来选择该股票的日线数据
    :param code:
    :param start:
    :param end:
    :return:
    """
    return ts.get_hist_data(code, start, end)


if __name__ == '__main__':
    #print(get_1day_tick('600848'))
    print(get_1day_tick('600848', start='2017-12-05', end='2017-12-29'))
