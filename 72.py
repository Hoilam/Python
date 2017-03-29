#!/usr/bin/python
# -*- coding:UTF-8 -*-

'''
read()方法从一个打开的文件中读取一个字符串。需要重点注意的是

'''


#打开一个文件
fo = open("foo.txt","r+")
str = fo.read(10);

print "读取的字符串是:",str

#关闭打开的文件
fo.close()
