#-*- coding:utf-8 -*-
# Deque: double-ended queue
class Deque:
	def __init__(self):
		self.items = []
	def addFront(self, item):
		self.items.append(item)
	def addRear(self, item):
		self.items.insert(0, item)
	def removeFront(self):
		return self.items.pop()
	def removeRear(self):
		return self.items.pop(0)
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)


d = Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())


# 回文字符串测试
def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)

	stillEqual = True

	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))






