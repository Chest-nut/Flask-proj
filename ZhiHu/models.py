#encoding:utf-8
# 数据库表模型文件

from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# 用户表模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, *args, **kwargs):
        telephone = kwargs.get('telephone')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.telephone = telephone
        self.username = username
        # 密码经过加密保存到数据库中
        self.password = generate_password_hash(password)

    # 密码验证方法
    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


# 文章表模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # datetime.now在每次插入记录时执行，datetime.now()只在创建表时执行也就是为固定值。
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref = db.backref('articles'))


# 用户评论表模型
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    article = db.relationship('Article', backref=db.backref('comments'))
    author = db.relationship('User', backref=db.backref('comments'))