#-*-coding:utf-8-*-
from cStringIO import StringIO
import os
import MySQLdb
from flask import Flask, request,session, g, redirect, url_for,render_template,flash,abort
from werkzeug import secure_filename
from flask import send_from_directory
from time import time
from flask_wtf.file import FileField
#from sqlalchemy import *
#import sqlalchemy.util as util
import string, sys
#from sqlalchemy.databases import mysql

app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload_images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.config.update(
    # DATABASE = '/flaskr.db',
    DEBUG = True,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    SECRET_KEY = 'xichao secret',
    USERNAME = 'xichao',
    PASSWORD = 'xichao123'
    )

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
   
@app.route("/")
def index():
    return render_template('welcome.html')

@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if session and session['logged_in']:
        return redirect('/admin/')
    error = None
    if request.method == 'POST':
        print request.form['username']
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
            #flash(error)
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
            #flash(error)
        else:
            session['logged_in'] = True
            #flash('You were logged in')
            return redirect('/admin/')
    return render_template('admin-login.html', error=error)
@app.route('/serve/')
def serve():
    return render_template("serve.html")

@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/humanity/')
def humanity():
    return render_template("humanity.html")

@app.route('/list/')
def list():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat')
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    article_list=[]
    try:
        cursor.execute("select * from xichao_article order by id DESC limit 100")
        article_list=cursor.fetchall()
    except:
        article_list='No article found'
    

    print (article_list)

    return render_template('list.html',list=article_list)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    #flash('You were logged out')
    return render_template('logout.html')


@app.route("/test/") 
def test():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    x=cursor.execute("select image_path,description from xichao_theme order by tid DESC limit 100")
    x=cursor.fetchall()
    
    all_path=[]
    all_desc=[]
    for item in x:
        all_path.append("../"+item['image_path'].encode('utf8'))
        all_desc.append(item['description'])
    
    print all_path
    print all_desc

    all_path=str(all_path).replace("\'","").strip("\'")[1:-1]
    all_desc=str(all_desc).replace("\'","").strip("\'")[1:-1]
    
    print all_path   
    return render_template('nav.html',all_path=all_path,all_desc=all_desc)


@app.route('/admin/', methods=['GET', 'POST'])
def upload_file():
    if session and session['logged_in']:
        conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
        conn.select_db('xichao_wechat');
        cursor = conn.cursor()
        cursor.execute("select * from xichao_article order by id DESC limit 1")
        data=None
        try:
            maxtid=cursor.fetchone()[0]
        except Exception:
            maxtid=0

        
        if request.method == 'POST':
            try:
                tid=request.form["tid_input"]
            except:
                tid=None
            
            


            if tid:
                try:
                    if request.form["preview2"]=='p2':
                        pre_text=request.form["editor2"]
                        return render_template("article.html",article=pre_text)
                except:
                    pass

                try:
                    file=request.files['image']
                    
                    
                    if file and allowed_file(file.filename):
                        file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
                        #save image
                        image_url=UPLOAD_FOLDER+file.filename
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        text=request.form["editor2"]
                        title=request.form["title"]
                        sql ="REPLACE INTO XICHAO_ARTICLE(id,title,image_path,article) values(%s,%s,%s,%s);"
                        par=(tid,title,image_url,text)
                        cursor.execute(sql,par)
                        cursor.close() 
                        conn.commit()
                        conn.close()
                        return "<h1>提交成功</h1><br/><a href='../admin'>返回继续提交</a>"
                    else:
                        abort(404,"please complete the form! image file: png jpeg gif jpg")  
                    
                    
                except:
                    abort(404,"please complete the form! image file: png jpeg gif jpg")  
                    
            else:    
                try:
                    text=request.form["editor1"]
                    
                    
                    try:
                        if request.form["preview1"]=='p1':
                            pre_text=request.form["editor1"]
                            return render_template("article.html",article=pre_text)
                    except:
                        pass
                    try:
                        file = request.files['image']
                    except:
                        abort(404,"please select a file")
                except:
                    abort(404,"please input id")
                
                if file and allowed_file(file.filename):
                    file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
                    #save image
                    image_url=UPLOAD_FOLDER+file.filename
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    title=request.form["title"]
                    sql = "insert into xichao_article(title,image_path,article) values(%s,%s,%s)"
                    par=(title,image_url,text)
                    cursor.execute(sql,par)
                    conn.commit()
                    cursor.close() 
                    conn.close()
                    return "<h1>提交成功</h1><br/><a href='../admin'>返回继续提交</a>"
                else:
                    abort(404,"please complete the form! image file: png jpeg gif jpg")  
                    
                
            
        return render_template("upload.html",maxtid=maxtid)
    else:
        abort(403,"permission denied")



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
    return render_template('article.html',article=text)


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor()
    cursor.execute("select * from xichao_comments order by tid")
    data=[]
    cur=1
    while True:
        try:
            data+=[{'text':str(cur)+'.'+cursor.fetchone()[1]}]
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
            order=(num+1,cm)
            sql = "insert into xichao_comments(tid,comment) values (%s,%s)"
            cursor.execute(sql,order)
            num+=1
    if cm!='':
       data+=[{'text':str(cur)+'.'+cm}]

    conn.commit()
    cursor.close() 
    conn.close()   
        
    return render_template("comment.html",comments=data,number=num)

if __name__ == "__main__":
    app.run(debug=True)
