#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql.cursors
# Before use pymysql module,install it,like this:"pip3 install pymysql"
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='222222',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
#print(type(connection))
try:
	with connection.cursor() as cursor:
		sql = "INSERT INTO `user` (`name`,`sex`) VALUES (%s,%s)"
		cursor.execute(sql,('yan','0'))
	connection.commit()
	with connection.cursor() as cursor:
		# sql = "SELECT * FROM `user` WHERE `name` = %s"
		# cursor.execute(sql,('yan'))
		sql = "SELECT * FROM `user`"
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)
finally:
	connection.close()
