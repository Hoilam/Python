#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 题目：求1 + 2！ + 3！+...+20!的和
# 程序分析：此程序只是把累加变成恶劣累乘

n = 0
s = 0
t = 1

for n in range(1,21):
	t *= n
	s += t

print '1! + 2! + 3! + ... + 20! = %d' % s



