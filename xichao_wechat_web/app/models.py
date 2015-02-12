#-*-coding:utf-8-*-
import os
import MySQLdb
import time
from flask import session


class Post:
	
	def __init__(self,default_config):
		self.db_host=default_config["db_host"]
		self.db_user=default_config["db_user"]
		self.db_passwd=default_config["db_passwd"]
		self.db_port=default_config["db_port"]
		self.db_name=default_config["db_name"]
		self.response = {'error': None, 'data': None}

    ## find items from id to id+limit
	def get_posts(self,category):
		conn=MySQLdb.connect(host=self.db_host,port=db_port,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article where category="+str(category)+" order by top desc,id desc;")
		posts=cursor.fetchall()
		conn.commit()
		conn.close()
		return posts

	def get_post_by_id(self,id):
		conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
		cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		cursor.execute("select * from xichao_article where id= "+str(id)+";")
		posts=cursor.fetchone()
		conn.commit()
		conn.close()
		return posts
	
	def add_new_post(self,post_data):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			
			#need to be sticked 
			if post_data[4]=="1":
				cursor.execute("update xichao_article set top=0 where top=1;")
			
			sql = "insert into xichao_article(title,image_path,article,category,top) values(%s,%s,%s,%s,%s);"
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
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
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

	def set_top(self,id):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			cursor.execute("update xichao_article set top=0 where top=1;")
			cursor.execute("update xichao_article set top=1 where id="+str(id))
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except Exception,e:
			self.response['error']=e
			return False
		
	def get_category_data(self):
		category_data=""
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
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
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
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

	def article_category(self):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			cursor.execute("select * from article_category")
			results=cursor.fetchall()
			cursor.close() 
			conn.commit()
			conn.close()
			article_category={}
			for item in results:
				article_category[item['id']]=item['name']
			return article_category
		except Exception,e:
			print e
			self.response['error']=e
			return {}
	def get_column_description(self):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			cursor.execute("select * from article_category")
			results=cursor.fetchall()
			cursor.close() 
			conn.commit()
			conn.close()
			column_description={}
			for item in results:
				column_description[item['id']]=item['description']
			return column_description
		except Exception,e:
			print e
			self.response['error']=e
			return {}
	def add_column(self,data):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql="INSERT INTO `article_category` (`name`,`description`) VALUES(%s,%s)"
			cursor.execute(sql, data)
			cursor.close() 
			conn.commit()
			conn.close()
			return True
		except Exception,e:
			print e
			self.response['error']=e
			return False

	def edit_column(self,data):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql ="update article_category set name=\""+data[1]+"\",description=\""+data[2]+"\"where id="+data[0]+";"
			cursor.execute(sql)
			cursor.close()
			conn.commit()
			conn.close()
			return True
		except Exception,e:
			self.response['error']=e
			return False
	def del_column(self,id):
		try:
			conn=MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,db=self.db_name,charset="utf8")
			cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			cursor.execute("delete from article_category where id="+str(id)+";")		
			cursor.close() 
			conn.commit()
			conn.close()
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
			self.response["error"]=str(e)
			self.response["data"]=str(e)

		self.response["data"]=self.user	
		return self.response

	
			
	def logout(self):
		if self.validate_login():
			self.session.pop('logged_in', None)
			return True
		return False


