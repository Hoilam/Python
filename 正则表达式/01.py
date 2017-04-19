#!/usr/bin/python
# -*- coding:UTF-8 -*-


import re

print (re.match('www','wwww.runoob.com').span())	#在起始位置匹配
print (re.match('com','www.runoob.com'))		#不在起始位置匹配：
