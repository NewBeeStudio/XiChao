from flask import Flask
from flask.ext.mail import Mail
from flask.ext.mail import Message
app = Flask(__name__)
mail = Mail(app)
# email server
##app.config.update(
##    MAIL_USE_SSL= True,
##    MAIL_USE_TLS=True, 
##    MAIL_SERVER='smtp.sina.com.cn',
##    MAIL_PORT=465,
##    MAIL_USERNAME='xichaoshudian',
##    MAIL_PASSWORD='xichao123'
##
##
##    )
app.config['MAIL_SERVER'] = 'smtp.163.com'
##app.config['MAIL_HOSTNAME'] = 'stmp.163.com'
app.config['MAIL_PORT'] = 465
##app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME'] = 'xichaoshudian@163.com'
app.config['MAIL_PASSWORD'] = 'xichao123'
 

ADMINS = ['xichaoshudian@163.com']
##msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
##msg.body = 'text body'
##msg.html = '<b>HTML</b> body'
##mail.send(msg)
@app.route("/")
def index():
    try:
        msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
        msg.body = 'text body'
        msg.html = '<b>HTML</b> body'
        mail.send(msg)
    except Exception,e:
        print e

    return "email sent!"

if __name__ == "__main__":
    app.run()
