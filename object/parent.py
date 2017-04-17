#!/usr/bin/python
# -*- coding:UTF-8 -*-


class parent:	#定义父类
	parentAttr = 100
	def __init__(self):
		print "调用父类构造函数"

	def parentMethod(self):
		print "调用父类方法"
	
	def setAttr(self,attr):
		parent.parentAttr = attr

	def getAttr(self):
		print "父类属性:",parent.parentAttr

class Child(parent):	#定义子类
	def __init__(self):
		print "调用子类构造方法"

	def childMethod(self):
		print '调用子类方法 child method'


c = Child()	#实例化子类
c.childMethod()	#调用子类的方法
c.parentMethod()	#调用父类方法
c.setAttr(200)	#再次调用父类的方法
c.getAttr()	#再次调用父类的方法





