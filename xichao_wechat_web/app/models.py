#-*-coding:utf-8-*-
import os
import MySQLdb
import time
from flask import session

class Post:
	
	def __init__(self,default_config):
		self.db_user=default_config["db_user"]
		self.db_passwd=default_config["db_passwd"]
		self.db_name=default_config["db_name"]
		self.response = {'error': None, 'data': None}

    ## find items from id to id+limit
	def get_posts(self,category):
		conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article where category="+str(category)+";")
		posts=cursor.fetchall()
		conn.commit()
		conn.close()
		return posts

	def get_post_by_id(self,id):
		conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article where id= "+str(id)+";")
		posts=cursor.fetchone()
		conn.commit()
		conn.close()
		return posts
	
	def add_new_post(self,post_data):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql = "insert into xichao_article(title,image_path,article,category) values(%s,%s,%s,%s)"
 			cursor.execute(sql,post_data)
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except Exception,e:
			self.response['error']=e
			return False

	def edit_post(self,post_data):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql ="REPLACE INTO xichao_article(id,title,image_path,article,category) values(%s,%s,%s,%s,%s);"
			cursor.execute(sql, post_data)
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except Exception,e:
			self.response['error']=e
			return False

		
	def get_category_data(self):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql ="select category,count(id) from xichao_article group by category order by category;"
 			cursor.execute(sql)
 			category_data=cursor.fetchall()
			cursor.close()
			conn.commit()
			conn.close()
			return category_data
		except Exception,e:
			self.response['error']=e
			return category_data
				
	def post_delete(self,id):
		try:
			conn=MySQLdb.connect(host='localhost',user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			cursor.execute("select image_path from xichao_article where id="+id+";")
			path=cursor.fetchone()["image_path"]
			cursor.execute("delete from xichao_article where id="+id+";")		
			path="static/upload_images/"+path
			#print 'path='+path
			cursor.close() 
			conn.commit()
			conn.close()
			os.remove(path)
			return True
		except Exception,e:
			print e
			self.response['error']=e
			
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


