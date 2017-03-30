#!/usr/bin/python
# -*- coding:UTF-8 -*-

#简单的例子，在该文件中的内容写入内容，但文件没有写入权限，发生异常
#在执行前,修改权限 chmod -w

try:
    fh = open("testFile","w");
    fh.write("这是一个测试文件，用于测试异常！！")
except IOError:
    print "Error:没有找到文件或读取文件失败"

else:
    print "内容写入文件成功"
    fh.close()



