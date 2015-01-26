#-*-coding:utf-8-*-
from cStringIO import StringIO
import os
import MySQLdb
from flask import Flask, request,session, \
     g, redirect, url_for,render_template,flash,abort
from flask.ext.mail import Mail
from flask.ext.mail import Message
import threading
from flask.ext.login import login_required
from werkzeug import secure_filename
from flask import send_from_directory
from flask import send_file
from time import time
from flask_wtf.file import FileField
#from sqlalchemy import *
#import sqlalchemy.util as util
import string, sys
from models import *
import json
import re
from config import *
from functions import *
#from sqlalchemy.databases import mysql

app = Flask(__name__)


admin=Admin(admin_config)
poster=Post(db_config)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 

@app.route("/")
def index():
    return render_template('welcome.html')

@app.route("/admin/")
def admin_index():
    if not admin.validate_login():
        abort(403)
    category_data=poster.get_category_data()
    cd=[0]*5
    print cd
    for num in category_data:
        print num
        cd[int(num["category"])-1]=int(num["count(id)"])
    print cd
    return render_template('admin.html',category_data=json.dumps(cd))

@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if admin.validate_login():
        return redirect('/admin/')  

    if request.method == 'POST':
        if not admin.login(request.form['username'],request.form['password'])["error"]:
            return redirect('/admin/')
    return render_template('login.html', error=admin.response['error'])

@app.route('/admin/logout/')
def logout():
    admin.logout()
    #flash('You were logged out')
    return render_template('logout.html')

@app.route('/admin/post/<string:column>/',methods=['GET', 'POST'])
def article_list(column):
    if not admin.validate_login():
        abort(403)
    column=column.lower()
    print 'colomn=',column
    if column in article_category.keys():
        category=article_category[column][0]
    else:
        abort(404)
    if request.method == 'POST':   
        id=request.form["id"] 
        id=id.strip()
        #print "id="+id
        poster.post_delete(id)
        #print "delete post!"
    article_list=poster.get_posts(category)
    #print article_list
    #flash('You were logged out')
    
    return render_template('tables.html',posts=reversed(article_list),column=article_category[column][1],url=column)

@app.route('/admin/post/<string:column>/edit/<int:tid>/',methods=['GET', 'POST'])
def edit(column,tid):
    if not admin.validate_login():
        abort(403)
    error=None
    post=None

    if request.method == 'POST':
        try:
            title=request.form["post-title"]
            text=request.form["post-full"]
            imagefile=request.files["image"]
            if imagefile and allowed_file(imagefile.filename):
                tmpfilename=str(int(time.time()))+'.'+imagefile.filename.rsplit('.', 1)[1]
                #save image
                image_url=UPLOAD_FOLDER+tmpfilename
                
                filename = secure_filename(tmpfilename)
                
                imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            category=article_category[column][0]
            post_data=(tid,title,filename,text,category)
            # print post_data

            if poster.edit_post(post_data):
                print "done"
                return render_template("edit.html",done=True,post=None,column=article_category[column][1])
            print poster.response
        except Exception,e:
            print e
            return render_template("edit.html",error=e,post=None,column=article_category[column][1])
    try:
        post=poster.get_post_by_id(tid)
        return render_template("edit.html",error=error,post=post,column=article_category[column][1])
    except Exception,e:
        error=str(e)
        return render_template("edit.html",error=e,post=post,column=article_category[column][1])    

@app.route('/admin/post/<string:column>/new/',methods=['GET', 'POST'])
def new_post(column):
    column=column.lower()
    if not admin.validate_login():
        abort(403)
    error=None
    if request.method == 'POST':
        try:
            title=request.form["post-title"]
            text=request.form["post-full"]
            imagedata=request.form["imagedata"]
            filename=datatofile(imagedata)
            category=article_category[column][0]
            post_data=(title,filename,text,category)
            # print post_data

            if poster.add_new_post(post_data):
                return render_template("new.html",done=True,column=article_category[column][1])
            print poster.response
        except Exception,e:
            print e
            return render_template("new.html",error=e,column=article_category[column][1])


    return render_template('new.html',column=article_category[column][1])


@app.route('/mobile/index/')
def mobile_index():
    return render_template("welcome.html")

@app.route('/admin/mobile/list/static/upload_images/<path:filename>')
@app.route('/mobile/list/static/upload_images/<path:filename>')
def image_src(filename):
    return send_from_directory('./static/upload_images/', filename)

@app.route('/mobile/list/<column>')
def mobile_list(column):
    if column in [key for key in article_category]:
        category_id=article_category[column][0]
        category=article_category[column][1]
    else:
        abort(404)
    posts=poster.get_posts(category_id)
    return render_template("list-yang.html",posts=reversed(posts),category=category)

@app.route('/mobile/article/<int:tid>/')
def mobile_article(tid):
    post=poster.get_post_by_id(tid)
    #print post
    category_id=post["category"]
    category=[item[1] for item in [article_category[key] for key in article_category] if item[0]==category_id][0]
    #print category
    return render_template('article.html',post=post,category=category)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    action = request.args.get('action')

    # 解析JSON格式的配置文件
    # 这里使用PHP版本自带的config.json文件
    with open(os.path.join(app.static_folder, 'ueditor', 'php',
                           'config.json')) as fp:
        try:
            # 删除 `/**/` 之间的注释
           
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}

    if action == 'config':
        # 初始化时，返回配置文件给客户端
        result = CONFIG

    if action in ('uploadimage', 'uploadvideo', 'uploadfile'):
        upfile = request.files['upfile']  # 这个表单名称以配置文件为准
        tmpfilename=str(int(time.time()))+'.'+upfile.filename.rsplit('.', 1)[1]
        #save image
        image_url=UPLOAD_FOLDER+tmpfilename
        filename = secure_filename(tmpfilename)
                # upfile 为 FileStorage 对象
        # 这里保存文件并返回相应的URL
        upfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = {
            "state": "SUCCESS",
            "url": "../../../../mobile/list/static/upload_images/"+filename,
            "title": "demo.jpg",
            "original": "demo.jpg"
        }
    return json.dumps(result)





