#-*-coding:utf-8-*-
import os, base64
import time
import urllib2
import json
import hashlib
from config import UPLOAD_FOLDER

def datatofile(data):
	imgtype=data.split(';')[0].split('/')[1]
	imgdata=data.split(';')[1].split(',')[1]
	imgData = base64.b64decode(imgdata)
	filename=str(int(time.time()))
	leniyimg = open(os.path.join('/home/xichao/git/XiChao/xichao_wechat_web/app/',UPLOAD_FOLDER)+filename+"."+imgtype,'w')
	leniyimg.write(imgData)
	leniyimg.close()
	return filename+"."+imgtype

	#all parameters are string type
def wechat_signature(url,appid,appsecret,noncestr,timestamp):
    access_token_url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+appsecret;
    access_token=json.loads(urllib2.urlopen(access_token_url).read().decode('utf-8')) 
    ticket_url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token='+access_token['access_token']+'&type=jsapi'
    ticket= json.loads(urllib2.urlopen(ticket_url).read().decode('utf-8'))
    string1='jsapi_ticket='+ticket['ticket']+'&noncestr='+noncestr+'&timestamp='+timestamp+'&url='+url
    return hashlib.sha1(string1).hexdigest()
