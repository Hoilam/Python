#!/usr/bin/python
# -*- coding:UTF-8 -*-


# re.match 函数
# 尝试从字符按串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match返回为
# none


# re.match(pattern,string,flags=0)
# pattern 匹配的正则表达式
# string 要匹配的字符串。
# flags 标志位，用于控制正则表达的匹配方式。如：是否区分大小写，多行等等


import re

line = "Cats are smarter than dogs"

matchobj =re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchobj:

	print "matchobj.group():",matchobj.group()
	print "matchobj.group(1):",matchobj.group(1)
	print "matchobj.group(2):",matchobj.group(2)
else:
	print "No match!!"
