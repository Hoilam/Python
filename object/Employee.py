#!/usr/bin/python
# -*- coding:UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:",self.name,", Salary:",self.salary


emp1 = Employee("FH",5000)
emp2 = Employee("hoilam",50000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" %Employee.empCount
