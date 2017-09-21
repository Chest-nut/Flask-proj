# -*- coding:utf-8 -*-

"""
装饰器文件

该模块用于管理所有自定义的装饰器
"""


from functools import wraps

from flask import session, redirect, url_for


def login_required(func):
    """用户未登录时跳转到登录页面"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
        
    return wrapper
