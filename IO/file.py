#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 读模式打开文件
f = open('/tmp/nginx.conf','r')
file_content = f.read()
# print(file_content)
# 关闭文件
f.close()

# try
try:
    f_protocal = open('/etc/protocols','r')
    # print(f_protocal.read())
finally:
    if f:
        f.close()

# with自动调用close方法
with open('/etc/profile','r') as f:
     print(f.read())

with open('/etc/hosts','r') as f_hosts:
    for line in f_hosts.readlines():
        print(line.strip())

# 写文件
with open('/tmp/write_test','w') as f:
    f.write('Hello there.')
