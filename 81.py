#!/usr/bin/python
# -*- coding:UTF-8 -*-

'''
try:
<语句>
finally:
<语句>  推出try时总会执行
raise
'''

try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常")
finally:
    print "Error：没有找到文件或读取文件失败"

