# -*- coding:utf-8 -*-

'''
主app文件
'''

from sqlalchemy import or_
from flask import Flask,render_template,request,session, redirect, url_for,g

import config
from exts import db
from decorators import login_required
from models import User, Article, Comment


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    """首页"""
    
    context ={
        'articles': Article.query.all()
    }
    # 获取数据库中所有文章记录，并渲染到首页
    return render_template('index.html', **context)


@app.route('/search/')
def search():
    """搜索功能"""
    
    q = request.args.get('q')
    articles = Article.query.filter(or_(Article.title.contains(q), Article.content.contains(q)))
    # 获取文章标题或内容中包含关键字q的记录，并渲染到首页
    return render_template('index.html', articles=articles)



@app.route('/login/', methods=['GET', 'POST'])
def login():
    """登录页面"""
    
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephone == telephone).first()
        #如果用户存在
        if user:
            #如果用户密码正确，用户id保存到session，并跳转到首页
            if user.check_password(password):
                session['user_id'] = user.id
                session.permanent = True
                print u'登陆成功'
                return redirect(url_for('index'))
            else:
                return u'密码不正确'
        else:
            return u'用户不存在'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    """注册页面"""
    
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        # 如果注册条件符合要求，将用户记录插入到数据库，并跳转到登录页面
        if not user:
            if password1 == password2:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                return u'两次输入的密码不一致'
        else:
            return u'该手机号码已注册'


@app.route('/publish/', methods=['GET', 'POST'])
@login_required
def publish():
    """发表话题页面"""
    
    if request.method == 'GET':
        return render_template('publish.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        # 将发表的文章记录插入数据库，并跳转到首页
        article = Article(title=title, content=content, author_id=g.user.id)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detial/<article_id>')
def detial(article_id):
    """文章详情页面"""
    
    article = Article.query.filter(Article.id==article_id).first()
    return render_template('detial.html', article=article)


@app.route('/logout/')
def logout():
    """注销功能"""
    
    session.clear()
    return redirect(url_for('login'))


@app.route('/comment/', methods=['POST'])
@login_required
def comment():
    """评论功能"""
    
    content = request.form.get('content')
    article_id = request.form.get('article_id')

    comment = Comment(content=content)
    comment.author=g.user
    comment.article_id=article_id
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detial', article_id=article_id))


@app.before_request
def my_bef_req():
    user_id = session.get('user_id')
    # 如果用户已登录，将用户模型对象保存到全局对象g，减少后续数据库查找操作
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


@app.context_processor
def my_con_pro():
    if hasattr(g,'user'):
        return {'user': g.user}
    return {}


if __name__ == '__main__':
    app.run()
