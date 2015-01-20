#-*-coding:utf-8-*-


UPLOAD_FOLDER = 'static/upload_images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db_config={
    "db_user":'root',
    "db_passwd":'root',
    'db_name':'xichao_wechat'  
}

admin_config={
    "user":'xichao',
    "passwd":'xichao123'
}
article_category={
                'nanyang':[1,u"0.48南洋荐书"],
                'shuzhi':[2,u"树枝态度"],
                'shishu':[3,u"嗜书瘾君子"],
                'qiuqiu':[4,u"一只球球"],
                'wendu':[5,u"曦潮温度"]
                }