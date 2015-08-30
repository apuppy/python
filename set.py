#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# set 保存Key,无重复 类似数学中无序且不重复的集合
s = set([1,2,2,3])
print(s)
# add
s.add(4)
s.add(4)
print(s)

# set 计算交集和并集
s2 = set([2,3,5])
total= s & s2
common = s | s2
print(total)
print(common)
