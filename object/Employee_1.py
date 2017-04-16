#!/usr/bin/python
# -*- coding:UTF-8 -*-

class Employee_1:
	'所有员工的基类'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee_1.empCount += 1
	
	def displayCount(self):
		print "Total Employee %d " % Employee_1.empCount

	def displayEmployee(self):
		print "Name : ",self.name,",Salary : ",self.salary

"创建Employee类的第一个对象"
emp1 = Employee_1("Zara",2000)
"创建Employee类的第二个对象"
emp2 = Employee_1("Manni",5000)

emp1.age = 7	#添加一个“age”属性


hasattr(emp1,'age')	
getattr(emp1,'age')


emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" %Employee_1.empCount






