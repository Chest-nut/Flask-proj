#encoding:utf-8
# 配置文件

from flask import session
import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhihu'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                          PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

