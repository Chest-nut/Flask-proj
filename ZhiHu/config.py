# 配置文件

#encoding:utf-8

import os

from flask import session

SECRET_KEY = os.urandom(24)

DEBUG = True

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
