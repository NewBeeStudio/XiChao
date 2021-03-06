#-*-coding:utf-8-*-
from cStringIO import StringIO
import os
import MySQLdb
from flask import Flask, request,session, \
     g, redirect, url_for,render_template,flash,abort,send_from_directory,send_file
import threading
from werkzeug import secure_filename
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

app.config.update(
    # DATABASE = '/flaskr.db',
    DEBUG = True,
    HOST=HOST,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    ARTICLE_TITLE_DEST=ARTICLE_TITLE_DEST,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    SECRET_KEY = 'xichao secret',
    USERNAME = admin_config["user"],
    PASSWORD = admin_config["passwd"],
    )

admin=Admin(admin_config)
poster=Post(db_config)
article_category=poster.article_category()
column_description=poster.get_column_description()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 

@app.route("/")
def index():
    article_category=poster.article_category()
    column_description=poster.get_column_description()
    return render_template('welcome.html',article_category=article_category,column_description=column_description)


@app.route("/admin/")
def admin_index():
    if not admin.validate_login():
        abort(403)
    article_category=poster.article_category()
    column_description=poster.get_column_description() 
    category_data=poster.get_category_data()
    
    return render_template('admin.html',article_category=article_category,column_description=column_description)

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

@app.route('/admin/column/',methods=['GET', 'POST'])   
def set_column():
    if not admin.validate_login():
        abort(403)
    article_category=poster.article_category()
    column_description=poster.get_column_description()
    if request.method == 'POST':
        try:
            new=request.form["new"]
            if new=='1':
                title=request.form["new_column_title"]
                description=request.form["new_column_description"]
                if poster.add_column((title,description)):
                    article_category=poster.article_category()
                    column_description=poster.get_column_description()
                    return redirect('/admin/')
                    #return render_template('set_column.html',article_category=article_category,column_description=column_description)
                else:
                    print poster.response
                    return redirect('/admin/')
                    #return render_template('set_column.html',article_category=article_category,column_description=column_description)

            elif new=='0':
                delete=request.form["del"]
                title=request.form["title"]
                description=request.form["description"]
                column_id=request.form["key"]
                if delete=="1":
                    if poster.del_column(column_id):
                        article_category=poster.article_category()
                        column_description=poster.get_column_description()
                        return redirect('/admin/')
                        #return render_template('set_column.html',article_category=article_category,column_description=column_description)
                    else:
                        print poster.response
                        return redirect('/admin/')
                        #return render_template('set_column.html',article_category=article_category,column_description=column_description)
                else:
                    if poster.edit_column((column_id,title,description)):
                        article_category=poster.article_category()
                        column_description=poster.get_column_description()
                        return redirect('/admin/')
                        #return render_template('set_column.html',article_category=article_category,column_description=column_description)
                    else:
                        print poster.response
                        return redirect('/admin/')
                        #return render_template('set_column.html',article_category=article_category,column_description=column_description)
        except Exception,e:
            print e
    return render_template('set_column.html',article_category=article_category,column_description=column_description)

@app.route('/admin/post/category/<int:column>/',methods=['GET', 'POST'])
def article_list(column):
    if not admin.validate_login():
        abort(403)
    article_category=poster.article_category()
    column_description=poster.get_column_description()

    if column in article_category.keys():
        category=column
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
    
    return render_template('tables.html',posts=article_list,column=article_category[column],url=column,article_category=article_category,column_description=column_description)

@app.route('/admin/post/category/<int:column>/edit/<int:tid>/',methods=['GET', 'POST'])
def edit(column,tid):
    if not admin.validate_login():
        abort(403)
    error=None
    post=None
    article_category=poster.article_category()
    column_description=poster.get_column_description()

    if request.method == 'POST':
        try:
            title=request.form["post-title"]
            text=request.form["post-full"]
            image_path=request.form["image_path"]
            
            try:
                top=request.form["top"]
            except:
                top="off"
            category=column
            post_data=(tid,title,image_path,text,category)
            # print post_data

            if poster.edit_post(post_data):
                if top=="on":
                    poster.set_top(tid)
                return render_template("edit.html",done=True,post=None,column=article_category[column],article_category=article_category,column_description=column_description)
            #print poster.response
        except Exception,e:
            print e
            return render_template("edit.html",error=e,post=None,column=article_category[column],article_category=article_category,column_description=column_description)
    try:
        post=poster.get_post_by_id(tid)
        return render_template("edit.html",error=error,post=post,column=article_category[column],article_category=article_category,column_description=column_description)
    except Exception,e:
        error=str(e)
        return render_template("edit.html",error=e,post=post,column=article_category[column],article_category=article_category,column_description=column_description)    

@app.route('/admin/post/category/<int:column>/new/',methods=['GET', 'POST'])
def new_post(column):
    if not admin.validate_login():
        abort(403)
    error=None
    article_category=poster.article_category()
    column_description=poster.get_column_description()

    if request.method == 'POST':
        try:
            title=request.form["post-title"]
            text=request.form["post-full"]
            image_path=request.form["image_path"]
            try:
                top=request.form["top"]
            except:
                top="off"


            
            
            category=column
            if top=="on":
                post_data=(title,image_path,text,category,"1")
            else:
                post_data=(title,image_path,text,category,"0")
                # print post_data
            print post_data
            if poster.add_new_post(post_data):
                return render_template("new.html",done=True,column=article_category[column],article_category=article_category,column_description=column_description)
       
           
            print poster.response
        except Exception,e: 
            print e
            return render_template("new.html",error=e,column=article_category[column],article_category=article_category,column_description=column_description)



    return render_template('new.html',column=article_category[column],article_category=article_category,column_description=column_description)


@app.route('/mobile/static/upload_images/<filename>')
def image_src(filename):
    return send_from_directory('/home/xichao/git/XiChao/xichao_wechat_web/app/static/upload_images/', filename)

@app.route('/mobile/list/category/<int:column>/')
def mobile_list(column):
    article_category=poster.article_category()
    column_description=poster.get_column_description() 

    if column in [key for key in article_category]:
        category_id=column
        category=article_category[column]
    else:
        abort(404)
    posts=poster.get_posts(category_id)
    
    return render_template("list-yang.html",posts=posts,category=category)

@app.route('/mobile/article/<int:tid>/')
def mobile_article(tid):

    post=poster.get_post_by_id(tid)
    # print post
    #category_id=post["category"]
    #category=[item[1] for item in [article_category[key] for key in article_category] if item[0]==category_id][0]
    #category=article_category[category_id]
    #print category
    url=request.url
    signature=wechat_signature(url,'wxf1186930550941c5','84bfbb6d5841fba82cb50cecf4f9721b','xichao','1414587457')
    
    return render_template('article.html',post=post,signature=signature,url=url)


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
        upfile.save(os.path.join('/home/xichao/git/XiChao/xichao_wechat_web/app/static/upload_images/',filename))
        # upfile.save(os.path.join('/Users/lixia/Documents/develop/github/Newbee/XiChao/xichao_wechat_web/app/static/upload_images/',filename))
        result = {
            "state": "SUCCESS",
            "url": HOST+"/mobile/static/upload_images/"+filename,
            "title": "demo.jpg",
            "original": "demo.jpg"
        }
    return json.dumps(result)

#######################################  图片裁剪器  #########################################

@app.route('/upload/tailor/title_image')
def upload_title_image():
    return render_template('upload_title_image_tailor.html')




##################################  美图秀秀配置文件  ##################################
@app.route('/crossdomain.xml')
def xiuxiu_config():
    return send_from_directory(os.path.dirname(__file__),'crossdomain.xml')


##文章题图上传路径
@app.route('/upload_article_title_image', methods=['GET', 'POST'])
def save_title_image():
    title_image = request.files['upload_file']
    #设置默认题图
    title_image_name = 'article_upload_pic_4.png'
    if title_image:
        if allowed_file(title_image.filename):
            title_image_name=get_secure_photoname(title_image.filename)
            title_image_url=os.path.join(app.config['ARTICLE_TITLE_DEST'], title_image_name)
            title_image.save(title_image_url)
    return app.config['HOST']+'/upload/article_title_image/'+title_image_name


#接收上传的题图文件，保存并返回路径
@app.route('/upload/title_image',methods=['GET', 'POST'])
def save_avatar():
    avatar = request.files['avatar']
    avatar_name='default.jpg'
    if avatar:
        if allowed_file(avatar.filename):
            avatar_name=get_secure_photoname(avatar.filename)
            avatar_url=os.path.join(app.config['ARTICLE_TITLE_DEST'],avatar_name)
            avatar.save(avatar_url)
    return '/upload/title_image/'+avatar_name


#获得文章题图
@app.route('/upload/article_title_image/<filename>')
def uploaded_article_title_image(filename):
    return send_from_directory(app.config['ARTICLE_TITLE_DEST'],filename)


