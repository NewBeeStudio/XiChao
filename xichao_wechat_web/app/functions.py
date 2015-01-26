#-*-coding:utf-8-*-
import os, base64
import time
from config import UPLOAD_FOLDER

def datatofile(data):
	imgtype=data.split(';')[0].split('/')[1]
	imgdata=data.split(';')[1].split(',')[1]
	imgData = base64.b64decode(imgdata)
	filename=str(int(time.time()))
	leniyimg = open(os.path.join(UPLOAD_FOLDER)+filename+"."+imgtype,'wb')
	leniyimg.write(imgData)
	leniyimg.close()
	return filename+"."+imgtype
