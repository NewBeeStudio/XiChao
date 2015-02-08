#-*-coding:utf-8-*-
from xichao import app
from config import *

app.config.update(
    # DATABASE = '/flaskr.db',
    DEBUG = True,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    SECRET_KEY = 'xichao secret',
    USERNAME = admin_config["user"],
    PASSWORD = admin_config["passwd"],
    PER_PAGE=15,

     #EMAIL SETTINGS
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME = 'xichaoshudian@163.com',
    MAIL_PASSWORD = 'xichao123'
    )

if __name__ == "__main__":
    app.run()