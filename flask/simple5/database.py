# -*- coding: utf-8 -*-
import pymysql

# 数据库连接
db_connection = None
def initial_db():
    global db_connection
    # MySQL配置
    connection = None
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='school'
    )
    db_connection = connection.cursor()



