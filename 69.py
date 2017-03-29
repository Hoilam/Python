#!/usr/bin/python
# -*- coding:UTF-8 -*-

#打开一个文件

fo = open("foo.txt","wb")
print "文件名:",fo.name
print "是否已关闭:",fo.closed
print "访问模式:",fo.mode
print "末尾是否强制加空:",fo.softspace
