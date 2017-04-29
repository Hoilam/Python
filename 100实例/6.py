#!/usr/bin/python
# -*- coding:UTF-8 -*-


# 题目：婓波那契数列 (Fibonacci sequence),又称黄金分割数列：0、1、1、2、3、5、# 8、13、21、34、........

# 在数学上，婓波那契数列是以递归的方法来定义：
# F0 = 0 （n = 0）
# F1 = 1 （n = 1）
# Fn = F[n - 1] + F[n - 2](n=>2)

# 方法一

# def fib(n):
#	a,b = 1,1
#	for i in range(n-1):
#		a,b = b,a+b
#	return a
#输出了第10个婓波那契数列
# print fib(10)


# 方法二

def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n-1)+fib(n-2)
# 输出了第10个婓波那契数列
print fib(10)



