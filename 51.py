#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time

#格式化成2016-03-20 0:00:09形式:
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


#格式成Sat Mar 00:00:12 2017形式
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())

#将格式字符串转换为时间戳
a = "Sat Mar 28 00:00:00 2017"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
