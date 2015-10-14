#!/usr/bin/python
# -*- coding: utf-8 -*-
'''更改当前文件夹下sample.ini的内容'''
import sys,ConfigParser
cf = ConfigParser.ConfigParser()
cf.read('sample.ini')
#获取配置段
section = sys.argv[1]
#配置名
key = sys.argv[2]
#配置值
value = sys.argv[3]
#k = cf.get(section,key)
#设置及写入配置文件
cf.set(section,key,value)
cf.write(open('sample.ini','w'))
