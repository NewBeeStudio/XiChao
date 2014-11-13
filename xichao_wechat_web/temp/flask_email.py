from flask import Flask
from flask.ext.mail import Mail
from flask.ext.mail import Message
app = Flask(__name__)
app.config.from_object(__name__)


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
app.config.update(
	EBUG=True,
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
