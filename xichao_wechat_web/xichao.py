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
    return render_template('index.html')

@app.route('/admin-login/', methods=['GET', 'POST'])
def login():
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
            return redirect('/upload/')
    return render_template('admin-login.html', error=error)

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


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if session and session['logged_in']:
        conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
        conn.select_db('xichao_wechat');
        cursor = conn.cursor()
        cursor.execute("select * from xichao_theme order by tid DESC limit 1")
        data=None
        try:
            maxtid=cursor.fetchone()[0]
        except Exception:
            maxtid=0

        if request.method == 'POST':
            file = request.files['image']
            title=request.form['title']
            text=request.form['text']
            description=request.form['description']
            
            if file and allowed_file(file.filename):
                file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
                print file.filename
                #save data  to db
                image_url=UPLOAD_FOLDER+file.filename
                data=(
                    maxtid+1,
                    image_url,
                    title,
                    description,
                    text
                    )
                print data
                sql = "insert into xichao_theme(tid,image_path,description,title,text) values (%s, %s, %s, %s,%s)"
                cursor.execute(sql,data)
                conn.commit()
                cursor.close() 
                conn.close() 

                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return '<script type="text/javascript" >alert("uploaded!");</script>'
        return render_template("upload.html",maxtid=maxtid)
    else:
        abort(403,"permission denied")

@app.route('/display', methods=['GET', 'POST'])
def uploaded():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='',charset="utf8") 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor()
    cursor.execute("select * from xichao_theme order by tid DESC limit 1")
    tid=0
    image_path=0
    description=0
    title=0
    text=0
    data=cursor.fetchone()
    if data:
        tid=data[0]
        image_path=data[1]
        description=data[2]
        title=data[3]
        text=data[4]
    
    return render_template('display.html',tid=tid,image_path=image_path,description=description,title=title,text=text)   

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='1234',charset="utf8") 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor()
    cursor.execute("select * from xichao_comments order by tid")
    data=[]
    while True:
        try:
            data+=[cursor.fetchone()[1]]
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
    s=''
    cur=1
    for i in data:
        s+=str(cur)+'.'+i+'d%2S'
        cur+=1
    if cm!='':
        s+=str(cur)+'.'+cm+'d%2S'
    s=s.rstrip('d%2S')
    conn.commit()
    cursor.close() 
    conn.close()   
        
    return render_template("comment.html",comment=s,number=num)

if __name__ == "__main__":
    app.run(debug=True)
