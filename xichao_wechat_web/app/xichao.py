#-*-coding:utf-8-*-
from cStringIO import StringIO
import os
import MySQLdb
from flask import Flask, request,session, g, redirect, url_for,render_template,flash,abort
from flask.ext.login import login_required
from werkzeug import secure_filename
from flask import send_from_directory
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
    PER_PAGE=15
    )

db_config={
    "db_user":'root',
    "db_passwd":''
}
admin_config={
    "user":app.config['USERNAME'],
    "passwd":app.config['PASSWORD']

}
admin=Admin(admin_config)
poster=Post(db_config)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
   
@app.route("/")
def index():
    return render_template('welcome.html')

@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if admin.validate_login():
        return redirect('/posts_list/')  

    if request.method == 'POST':
        if not admin.login(request.form['username'],request.form['password'])["error"]:
            return redirect('/posts_list/')
    return render_template('admin-login.html', error=admin.response['error'])

@app.route('/serve/')
def serve():
    return render_template("serve.html")

@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/humanity/')
def humanity():
    return render_template("humanity.html")

@app.route('/register/')
def register():
    return render_template("register.html")

def humanity():
    return render_template("humanity.html")

@app.route('/list/')
def list():
    article_list=poster.get_posts(0,10)
    return render_template('list.html',list=article_list)


@app.route('/admin/logout')
def logout():
    print admin.logout()
    #flash('You were logged out')
    return render_template('logout.html')



@app.route('/posts_list/', defaults={'page': 1})
@app.route('/posts_list/page-<int:page>')
def posts(page):
    if not admin.validate_login():
        abort(403)
    skip = (page - 1) * int(app.config['PER_PAGE'])
    posts = poster.get_posts(skip,int(app.config['PER_PAGE']))
    return render_template('posts.html', posts=posts)


@app.route('/newpost/',methods=['GET', 'POST'])
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
            return render_template("new_post.html",error=e)


    return render_template("new_post.html")

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
            sql = "insert into xichao_comments(tid,articleID,comment) values (%s,%s,%s)"
            cursor.execute(sql,order)
            num+=1
    if cm!='':
       data+=[{'text':str(cur)+'.'+cm}]

    conn.commit()
    cursor.close() 
    conn.close()   
        
    return render_template("comment.html",comments=data,number=num,id=id)



if __name__ == "__main__":
    app.run(debug=True)

