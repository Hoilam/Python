#!/usr/bin/python
# -*- coding:UTF-8 -*-


# 题目：判断101 - 200 之间有多少热素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2sqrt(这个数),如果能被整除，则表明# 此数不是素数，反之是素数。


h = 0
leap = 1

from math import sqrt
from sys import stdout

for m in range(101,201):
	k = int(sqrt(m + 1))
	for i in range(2,k + 1):
		if m % i == 0:
			leap = 0
			break
	if leap == 1:
		print '%-4d' % m
		h += 1
		if h % 10 == 0:
			print ''
	leap = 1
print 'The total is %d' % h


		

	
