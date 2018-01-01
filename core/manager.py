import pandas as pd
import tushare as ts
from core.get_1min_tick import get_1min_tick
from core.get_all_stock_code import get_all_stock_code_from_file
from core.log import logger
from mysql.mysql_connection import get_mysql_connection
from utils.write_to_file import write_to_excel
from concurrent.futures import ThreadPoolExecutor, wait


def task(writer, code_list, ts_connection):
    """
    子任务：用于下载数据
    :param writer:
    :param code_list:
    :param ts_connection:
    :return:
    """
    logger.info(code_list)
    for code in code_list:
        logger.info("processing : %s" % code)
        for i in range(5):
            try:
                df = get_1min_tick(code, ts_connection)
                write_to_excel(writer, code, df)
                break
            except IOError as e:
                logger.info(e)
                logger.info("Retrying..." + code)


def executor_manager(writer, all_code_list, ts_connection):
    """
    线程池管理器
    :return:
    """
    executor = ThreadPoolExecutor(max_workers=10)
    future_list = []

    for i in range(10):
        future = executor.submit(task, writer, all_code_list[i * 2:(i + 1) * 2], ts_connection)
        future_list.append(future)

    wait(future_list)

    logger.info('所有股票数据更新完毕')


if __name__ == "__main__":
    mysql_connection = get_mysql_connection()
    ts_connection = ts.get_apis()
    all_code_list = get_all_stock_code_from_file()
    all_code_list = ["002506", "600703", "300059", "600206", "002281",
                     "603345", "002555", "002440", "600897", "000063"]
    writer = pd.ExcelWriter('./../file/1min.xlsx')

    executor_manager(writer, all_code_list, ts_connection)

    writer.save()
    mysql_connection.close()
    pass
