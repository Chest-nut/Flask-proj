#encoding:utf-8
# 装饰器文件

from functools import wraps
from flask import session, redirect, url_for

# 用户未登录时跳转到登录页面
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
