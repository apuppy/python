#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
# os name
print('OS name:%s' %(os.name))
# os uname only used for *nix system
os_uname = os.uname()
print(type(os_uname))

# environment path
os_path = os.environ
# 获取某个环境变量的值
print('PATH :%s' %os.environ.get('PATH'))
# 获取当前文件的绝对路径
abs_path = os.path.abspath('.')
print('absolute path is:%s' %abs_path)

# join split 这类方法并不要求目录或文件真实存在，对字符亦可操作
#表示路径用join 创建目录 删除目录
new_dir = os.path.join(os.path.abspath('.'),'test_dir')
#print(new_dir)
#os.mkdir(new_dir)
#os.rmdir(new_dir)

# 拆分文件与路径名
mail_log = os.path.split('/var/log/maillog')
print(mail_log)
# 获取扩展名
mail_log_ext = os.path.splitext('./file.py')
print(mail_log_ext)

# 文件重命名与删除
os.rename('/tmp/test.txt','/tmp/test.py')
os.remove('/tmp/test.py')
# 复制文件 shutil copyfile()
