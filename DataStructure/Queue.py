#-*- coding:utf-8 -*-
# Queue
# FIFO
class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

q = Queue()

q.enqueue('King')
print(q.size())
print(q.isEmpty())
q.enqueue(9.9)
print(q.dequeue())
print(q.dequeue())
print(q.size())


# 模拟击鼓传花
def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))


# 模拟打印机工作
class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60 / self.pagerate


import random

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
	
	labprinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingtimes = []

	for currentSecond in range(numSeconds):

		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)

		labprinter.tick()

	averageWait = sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


def newPrintTask():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	else:
		return False


for i in range(10):
	simulation(3600, 5)










