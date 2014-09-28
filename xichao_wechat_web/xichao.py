from flask import render_template
import flask
from cStringIO import StringIO
import os
import MySQLdb
from flask import Flask, request, redirect, url_for
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








    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
   

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/testmysql/")
def testmysql():
    return str(desctext)


@app.route("/test/")
def test():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='') 
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
   
    print all_path
   
    return render_template('nav.html',all_path=all_path,all_desc=all_desc)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    conn = MySQLdb.connect(host='localhost', user='root',passwd='') 
    conn.select_db('xichao_wechat');
    cursor = conn.cursor()
    cursor.execute("select * from xichao_theme order by tid DESC limit 1")
    data=cursor.fetchone()[0]
    maxtid=0
    if data:
       maxtid=data
    print type(maxtid)
    desctext= cursor.description



    if request.method == 'POST':
        file = request.files['image']
        title=request.form['title']
        text=request.form['text']
        description=request.form['description']
        if file and allowed_file(file.filename):
            file.filename=str(int(time()))+'.'+file.filename.rsplit('.', 1)[1]
            
            #save data  to db
            image_url=UPLOAD_FOLDER+file.filename
            data=(
                int(maxtid+1),
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
@app.route('/upload_images/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    return '<script type="text/javascript" >alert("uploaded!");</script>'






if __name__ == "__main__":
    app.run(debug=True)

