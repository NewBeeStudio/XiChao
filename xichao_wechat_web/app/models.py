#-*-coding:utf-8-*-
import os
import MySQLdb
from flask import session

class Post:
	
	def __init__(self,default_config):
		self.db_user=default_config["db_user"]
		self.db_passwd=default_config["db_passwd"]


    ## find items from id to id+limit
	def get_posts(self,id,limit):
		conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db="xichao_wechat",charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article limit "+str(id)+","+str(limit))
		return cursor.fetchall()

	def get_post_by_id(self,id):
		conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db="xichao_wechat",charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article where id= "+str(id))
		return cursor.fetchone()
	
	def add_new_post(self,post_data):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db="xichao_wechat",charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql = "insert into xichao_article(title,image_path,article) values(%s,%s,%s)"
 			cursor.execute(sql,post_data)
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except:
			return False

	def edit_post(self,post_data):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db="xichao_wechat",charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql ="REPLACE INTO XICHAO_ARTICLE(id,title,image_path,article) values(%s,%s,%s,%s);"
 			cursor.execute(sql,post_data)
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except:
			return False
	def post_delete(self,id):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db="xichao_wechat",charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql ="delete from XICHAO_ARTICLE where id="+id
			cursor.execute(sql)
			cursor.close() 
			conn.commit()
			conn.close()
			return True
		except:
			return False







class Admin:
	def __init__(self,default_config):
		self.user=default_config["user"]
		self.passwd=default_config["passwd"]
		self.response = {'error': None, 'data': None}
		self.session=session

	def validate_login(self):
		if self.session and self.session['logged_in']:
			return True
		return False

	def login(self,inputuser,inputpasswd):
		if self.validate_login():
			return self.response
		try:
			if inputuser!=self.user:
				self.response["error"]="Invalid username"
			elif inputpasswd!=self.passwd:
				self.response["error"]="Invalid password"
			else:
				session['logged_in'] = True
					
		except Exception,e:
			self.response["error"]="system error"
			self.response["data"]=str(e)

		self.response["data"]=self.user	
		return self.response

	
			
	def logout(self):
		if self.validate_login():
			self.session.pop('logged_in', None)
			return True
		return False


