#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 题目:求s=a+aa+aaa+aaaa+aa....a的值,其中a是一个数字.例如2+22+222+2222+222# 22(此时共有5个数相加),几个数相加由键盘控制。

# 程序分析:关键是计算出每一项的值。

Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a ='))
for count in range(n):
	Tn = Tn + a
	a = a * 10
	Sn.append(Tn)
	print Tn



Sn = reduce(lambda x,y : x + y,Sn)
print "计算和为:",Sn


