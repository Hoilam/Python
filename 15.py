#!/usr/bin/python
# -*- coding:UTF-8 -*-

a = 10
b = 20
list = [1,2,3,4,5];

if (a in list ):
	print "1 - 变量a在给定的列表中list中"
else:
	print "1 - 变量a不在给定的列表中list中"

if (b not in list ):
	print "2 - 变量b不在给定的列表中list中"
else:
	print "2 - 变量b在给定的列表中list中"

# 修改变量a的值
a = 2
if (a in list):
	print "3 - 变量a在给定的列表中list中"
else:
	print "3 - 变量a不在给定的列表中list中"
