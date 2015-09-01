#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,age):
        self.name = name
	self.age = age
    def info(self):
	print('%s:%s' %(self.name,self.age))

aStudent = Student('sophia',22)
aStudent.info()

# 私有变量以__开头加变量名 __var
class boy(object):
    def __init__(self,name,age,sex):
        self.name = name
	self.__age = age
	self.sex = sex
    def self_desc(self):
	print('My name is %s,a %s,%s years old.' %(self.name,self.sex,self.__age))

someone = boy('kevin',22,'male');
someone.self_desc();
"""
private_age = someone._boy__age
print(private_age)
"""
# 以_开头的变量外部可以访问，但是其目的是标示出来，建议不在外部访问
# 以双划线开头并以双划线结尾的变更是特殊变量
# 以又划线开头的变量其实仍可访问，但是不建议 someone._boy__age
