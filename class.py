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
