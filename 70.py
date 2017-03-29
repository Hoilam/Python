#!/usr/bin/python
# -*- coding:UTF-8 -*-

# close()函数

fo = open("foo.txt","wb");
print "文件名:",fo.name

#关闭打开的文件
fo.close()
