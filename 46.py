#!/usr/bin/python
# -*- coding:UTF-8 -*-

dict = {'Name':'Zara','Age':7,'Class':'First'};

del dict['Name']; #删除键是‘Name’的条目
print dict['Age'];
dict.clear(); #清空词典所有条目

del dict;

print "dict['Age']:",dict['Age'];
print "dict['School']:",dict['School'];
