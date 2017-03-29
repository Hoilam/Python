#!/usr/bin/python
# -*- coding:UTF-8 -*-

'''
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，
Python字符串可以是二进制数据，而不是仅仅是文字。
write()方法不会在字符串的结尾添加换行符('\n')

'''


#打开一个文件
fo = open("foo.txt","wb")
fo.write("www.runoob.com!\nVery good site!\n");

#关闭打开的文件
fo.close()

#该方法会创建foo.txt文件，并将收到的内容写入该文件。
