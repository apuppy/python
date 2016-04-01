#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sts = (1,2,3)
print(type(sts))
# only one
single_element_tuple = ('kevin',)
print(single_element_tuple)
print(single_element_tuple[0])
# '可变的tuple',其实是指向不变
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
