#!/usr/bin/python
# -*- coding:UTF-8 -*-



# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数
# 返回None;而re.search匹配整个字符串，直到找到一个匹配

import re

line = "Cate are smarter than dogs";

matchObj = re.match(r'dogs',line,re.M|re.I)

if matchObj:
	print 'match --> matchObj.group():',matchObj.group()
else:
	print "No match!"


matchObj = re.search(r'dogs',line,re.M|re.I)

if matchObj: 
	print "search --> matchObj.group():",matchObj.group()
else:
	print "No match!!"
