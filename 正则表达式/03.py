#!/usr/bin/python
# -*- coding:UTF-8 -*-

# re.search 函数
# re.search(pattern,string,flags=0)

# pattern 匹配的正则表达式
# string 要匹配的字符串
# flags 标志位，用于控制正则表达式

import re

print (re.search('www','www.runoob.com').span())	#在起始位置匹配
print (re.search('com','www.runoob.com').span())	#不在起始位置匹配



