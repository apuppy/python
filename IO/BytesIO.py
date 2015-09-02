#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 操作二进制数据
from io import BytesIO
f = BytesIO()
# 写入字符经过utf-8编码后的bytes
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 与StringIO类似，也可以初始化时传入bytes，再读取
bytes = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
bytes_str = bytes.read()
print(bytes_str)
