import tushare as ts


def get_all_stock_code():
    """
    使用tushare获得所有股票代码
    :return: 股票代码列表
    """
    df = ts.get_stock_basics().reset_index()
    return df['code'].tolist()

def get_all_stock_code_from_file():
    """
    从本地股票列表文件中，获得所有股票代码
    :return: 股票代码列表
    """
    with open("./../file/stock_list") as file:
        return file.readline().split(",")
    pass

if __name__ == '__main__':
    a = get_all_stock_code_from_file()
    print(a)
