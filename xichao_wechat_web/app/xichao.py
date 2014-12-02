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
#from sqlalchemy.databases import mysql

app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload_images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config.update(
    # DATABASE = '/flaskr.db',
    DEBUG = True,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    SECRET_KEY = 'xichao secret',
    USERNAME = 'xichao',
    PASSWORD = 'xichao123',
    PER_PAGE=15,

     #EMAIL SETTINGS
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME = 'xichaoshudian@163.com',
    MAIL_PASSWORD = 'xichao123'
    )

db_config={
    "db_user":'root',
    "db_passwd":'1234',
    'db_name':'xichao_wechat'  
}
admin_config={
    "user":app.config['USERNAME'],
    "passwd":app.config['PASSWORD']

}
article_category={
                'nanyang':[1,u"0.48南洋荐书"],
                'shuzhi':[2,u"树枝态度"],
                'shishu':[3,u"嗜书瘾君子"],
                'qiuqiu':[4,u"一只球球"],
                'wendu':[5,u"曦潮温度"]
                }

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
    return render_template('admin.html')

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
    if column in [key for key in article_category]:
        category=article_category[column][0]
    else:
        abort(404)
    if request.method == 'POST':   
        id=request.form["id"] 
        id=id.strip()
        print "id="+id
        poster.post_delete(id)
        print "delete post!"
    article_list=poster.get_posts(category)
    print article_list
    #flash('You were logged out')
    
    return render_template('tables.html',posts=article_list,column=article_category[column][1])


@app.route('/admin/post/<string:column>/edit/<int:tid>/',methods=['GET', 'POST'])
def edit(column,tid):
    if not admin.validate_login():
        abort(403)

    column=column.lower()
    category=article_category[column][0]

    #post=get_article from db
    return render_template('edit.html',post=post,column=article_category[column][1])

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
            imagefile=request.files["image"]
            if imagefile and allowed_file(imagefile.filename):
                tmpfilename=str(int(time.time()))+'.'+imagefile.filename.rsplit('.', 1)[1]
                #save image
                image_url=UPLOAD_FOLDER+tmpfilename
                
                filename = secure_filename(tmpfilename)
                
                imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            category=article_category[column][0]
            post_data=(title,filename,text,category)
            # print post_data

            if poster.add_new_post(post_data):
                return render_template("edit.html",done=True,column=article_category[column][1])
            print poster.response
        except Exception,e:
            print e
            return render_template("edit.html",error=e,column=article_category[column][1])


    return render_template('edit.html',column=article_category[column][1])


@app.route('/mobile/index/')
def mobile_index():
    return render_template("welcome.html")

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
    return render_template("list-yang.html",posts=posts,category=category)

@app.route('/mobile/article/<int:tid>/')
def mobile_article(tid):
    post=poster.get_post_by_id(tid)
    print post
    category_id=post["category"]
    category=[item[1] for item in [article_category[key] for key in article_category] if item[0]==category_id][0]
    print category
    return render_template('article.html',post=post,category=category)


#####################################################################################################
#mail = Mail(app)
#ADMINS = ['xichaoshudian@163.com']

# def send_async_email(msg):
#     with app.app_context(): #otherwise, runtimeERROR:working outside of application context
#         mail.send(msg)
        
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        try:
            msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
            msg.body = 'text body'
            msg.html =  str(request.form)
##            msg.html+="<br>"+request.form.get('fullname')+"<br>"+request.form.get('gender')+"<br>"+request.form.get('school')+"<br>"+request.form.get('grade')+\
##                       "<br>"+request.form.get('email')+"<br>"+request.form.get('favcolor')+"<br>"+request.form.get('addinfo')
            for item in request.form:
                msg.html+="<br>"+str(item)+":"+request.form.get(str(item))
            thr = threading.Thread(target = send_async_email, args = [msg])
            thr.start()
        except Exception,e:
            print e

    return render_template("register.html")



@app.route('/list/')
def list():
    article_list=poster.get_posts(0,10)
    return render_template('list.html',list=article_list)






@app.route('/posts_list/', defaults={'page': 1})
@app.route('/posts_list/page-<int:page>')
def posts(page):
    if not admin.validate_login():
        abort(403)
    skip = (page - 1) * int(app.config['PER_PAGE'])
    posts = poster.get_posts(skip,int(app.config['PER_PAGE']))
    return render_template('posts.html', posts=posts)


@app.route('/newpost/',methods=['GET','POST'])
def newpost():
    if not admin.validate_login():
        abort(403)
    error=None
    if request.method == 'POST':
        try:
            
            title=request.form["post-title"]
           
            text=request.form["post-full"]
            
            file=request.files['image']
            if file and allowed_file(file.filename):
                file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
                #save image
                image_url=UPLOAD_FOLDER+file.filename
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            post_data=(title,image_url,text)
            print post_data
            if poster.add_new_post(post_data):
                return "<h1>提交成功</h1><br/><a href='../newpost/'>返回继续提交</a>"
        except Exception,e:
            print e
            return render_template("test.html",error=e)


    return render_template("test.html")

@app.route('/post_edit<id>',methods=['GET', 'POST'])
def post_edit(id):
    if not admin.validate_login():
        abort(403)
    post = poster.get_post_by_id(id)
    tid=post["id"]
    print tid
    if request.method == 'POST':
        try:
            title=request.form["post-title"]
            text=request.form["post-full"]
            file=request.files['image']
            if file and allowed_file(file.filename):
                file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
                #save image
                image_url=UPLOAD_FOLDER+file.filename
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            post_data=(tid,title,image_url,text)
            
            if poster.edit_post(post_data):
                return "<h1>修改成功</h1><br/><a href='../posts_list/'>返回列表</a>"          
        except Exception,e:
            return render_template("new_post.html",error=e)

    
    return render_template('edit_post.html',post=post)

@app.route('/post_delete<id>')
def post_del(id):
    if not admin.validate_login():
        abort(403)
    if poster.post_delete(id):
        return "<h1>删除成功</h1><br/><a href='../posts_list/'>返回列表</a>" 
    abort(404)
    
@app.route('/t/<id>')
def article(id):
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat')
    cursor = conn.cursor()
    text=''
    try:
        cursor.execute("select article from xichao_article where id="+id)
        text=cursor.fetchone()[0]
    except:
        text='No article found'
    cursor.close() 
    conn.close()
    return render_template('article.html',article=text,id=str(id))


@app.route('/comment/<id>', methods=['GET', 'POST'])
def comment(id):
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor()
    cursor.execute("select * from xichao_comments  where articleID="+id)
    data=[]
    cur=1
    while True:
        try:
            data+=[{'text':str(cur)+'.'+cursor.fetchone()[2]}]
            cur+=1
        except:
            break
    cursor.execute("select count(*) as value from xichao_comments ")
    num=cursor.fetchone()[0]
    num=int(num)
    cm=''
    if request.method == 'POST':       
        cm=request.form['text']
        if cm!='':
            articleID=id
            order=(num+1,articleID,cm)           
            sql = "insert into xichao_comments(comment_id,articleID,comment) values (%s,%s,%s)"
            cursor.execute(sql,order)
            num+=1
    if cm!='':
       data+=[{'text':str(cur)+'.'+cm}]

    conn.commit()
    cursor.close() 
    conn.close()   
        
    return render_template("comment.html",comments=data,number=num,id=id)



if __name__ == "__main__":
    app.run()

