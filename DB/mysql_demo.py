#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql.cursors
# Before use pymysql module,install it,like this:"pip3 install pymysql"
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
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
"""
CREATE TABLE user (
	id int(11) unsigned not null auto_increment primary key,
	name varchar(32) not null default '',
	sex tinyint(1) not null default 0,
	created_time datetime not null default CURRENT_TIMESTAMP
)engine = InnoDB default charset = utf8;
"""
