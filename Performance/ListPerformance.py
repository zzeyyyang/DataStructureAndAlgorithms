#-*- coding:utf-8 -*-
from timeit import Timer


def test1():
	l = []
	for i in range(1000):
		l += [i]  # O(k), k为进行连接的list长度


def test2():
	l = []
	for i in range(1000):
		l.append(i)  # O(1)


def test3():
	l = [i for i in range(1000)]  # list comprehension


def test4():
	l = list(range(1000))  
	# Python2: range()返回一个list, xrange()返回一个可迭代的对象, 更节省内存
	# Python3: range()相当于Python2中的xrange()


t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")


