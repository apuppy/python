#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 内存中写入数据
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
# getvale()用于获取写入的值
print(f.getvalue())

#读取初始化StringIO()传入的值
str = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = str.readline()
    if s == '':
        break
    print(s.strip())
