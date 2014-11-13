from flask import Flask, request,\
      redirect, url_for,render_template,flash
from flask.ext.mail import Mail
from flask.ext.mail import Message
app = Flask(__name__)
app.config.from_object(__name__)
import threading

app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.163.com',
	MAIL_PORT=25,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL=False,
	MAIL_USERNAME = 'xichaoshudian@163.com',
	MAIL_PASSWORD = 'xichao123'
	)


mail = Mail(app)
ADMINS = ['xichaoshudian@163.com']

def send_async_email(msg):
    with app.app_context(): #otherwise, runtimeERROR:working outside of application context
        mail.send(msg)
    
@app.route("/", methods=['GET', 'POST'])
def index():
    print 'start!'
    if request.method=='POST':
        print 'post!'
        try:
##            name=request.form['name']
##            gender=request.form['gender']
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


    return render_template('register.html')

if __name__ == "__main__":
    app.run()
