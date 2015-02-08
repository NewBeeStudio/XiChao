#-*-coding:utf-8-*-
from app.xichao import app
from app.config import *

app.config.update(
    # DATABASE = '/flaskr.db',
    DEBUG = True,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    SECRET_KEY = 'xichao secret',
    USERNAME = admin_config["user"],
    PASSWORD = admin_config["passwd"],
    )

if __name__ == "__main__":
    app.run()