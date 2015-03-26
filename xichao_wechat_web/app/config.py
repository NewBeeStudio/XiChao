#-*-coding:utf-8-*-
import os

UPLOAD_FOLDER = 'static/upload_images/'
ARTICLE_TITLE_DEST = os.path.join(os.path.dirname(__file__), 'upload/title_image')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

HOST='http://wechat.xichao-o.com'

db_config={
    "db_host":'rdszfuv6jmjjbei.mysql.rds.aliyuncs.com',
    "db_user":'xichao',
    "db_passwd":'Xichao42',
    "db_port":3306,
    'db_name':'xichao_wechat'  
}

admin_config={
    "user":'xichao',
    "passwd":'xichao123'
}

##############################
# runserver.py
# HOST='http://127.0.0.1:5000'

# db_config={
#     "db_host":'localhost',
#     "db_user":'root',
#     "db_passwd":'root',
#     "db_port":3306,
#     'db_name':'xichao_wechat'  
# }