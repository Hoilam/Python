#!/usr/bin/python
# -*- coding:UTF-8 -*-

# re.sub(pattern ,repl ,strin ,count=0 ,flags=0)

# pattern:正则中的模式字符串。
# repl: 替换的字符串，也可为一个函数。
# string: 要被查找替换的原始字符串。
# count: 模式匹配后替换的最大次数，默认0表示替换所有的匹配。


import re

phone = "2004-959-559 #这是一个国外的电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是：",num


# 删除非数字（-）的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是：",num









