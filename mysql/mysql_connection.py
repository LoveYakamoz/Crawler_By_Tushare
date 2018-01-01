import pymysql


def get_mysql_connection():
    """
    获得mysql数据库的链接
    :return:
    """
    conn = pymysql.connect("localhost", "root", "root", "stock")
    return conn