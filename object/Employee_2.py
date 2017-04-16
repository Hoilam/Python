#!/usr/bin/python
# -*- coding:UTF-8 -*-

class Employee_2:
	'所有员工的基类'
	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name: ",self.name, "Salary:", self.salary


print "Employee_2.__doc__:",Employee_2.__doc__
print "Employee_2.__name__:",Employee_2.__name__
print "Employee_2.__module__:",Employee_2.__module__
print "Employee_2.__bases__:",Employee_2.__bases__
print "Employee_2.__dict__:",Employee_2.__dict__
