#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector
mysql_conn = mysql.connector.connect(host='localhost',database='test',user='root',password='123456')
print(vars(mysql_conn))
