#!/usr/bin/python
# -*- coding:UTF-8 -*-

a = 20
b = 20

if ( a is b ):
	print "1 - a 和 b 有相同的标识"
else:
	print "1 - a 和 b没有相同的标识"

if (id(a) is not id(b)):
	print "2 - a 和 b 有相同的标识"
else:
	print "2 - a 和 b 没有相同的标识"

# 修改变量b的值
b = 30
if ( a is b):
	print "3 - a 和 b 有相同的标识"
else:
	print "3 - a 和 b 没有相同的标识"

if ( a is not b):
	print "4 - a 和 b 没有相同的标识"

else:
	print "4 - a 和 b 有相同的标识"
