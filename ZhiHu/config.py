# -*- coding:utf-8 -*-

"""
配置文件


这里包含session所需的盐，以及数据库相关配置
"""


import os

from flask import session


SECRET_KEY = os.urandom(24)     # 盐

# DEBUG = True

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'xxx'
PASSWORD = 'xxx'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'xxx'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                          PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
