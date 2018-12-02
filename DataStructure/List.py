# Linked List
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class UnorderedList:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		current = self.head
		temp = Node(item)
		while current.getNext() != None:
			current = current.getNext()

		current.setNext(temp)

	def insert(self, pos, item):
		current = self.head
		temp = Node(item)
		previous = None
		loc = 0
		while loc != pos:
			loc += 1
			previous = current
			current = current.getNext()

		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			previous.setNext(temp)
			temp.setNext(current)

	def index(self, item):
		current = self.head
		found = False
		loc = 0
		while current.getNext() != None and not found:
			if current.getData() == item:
				found = True
			else:
				loc += 1
				current = current.getNext()

		return loc

	def pop(self, pos):
		current = self.head
		previous = None
		loc = 0
		while loc != pos:
			loc += 1
			previous = current
			current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

		return current

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()

		return count


mylist = UnorderedList()
print(mylist.isEmpty())
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
print(mylist.size())
print(mylist.search(31))
mylist.append(99)
print(mylist.size())
print(mylist.index(26))
mylist.insert(1, 29)
print(mylist.index(29))
print(mylist.index(93))
mylist.remove(29)
print(mylist.search(29))
print(mylist.index(93))
print(mylist.index(31))
mylist.pop(0)
print(mylist.search(26))
print(mylist.index(31))
print(mylist.size())


# OrderedList
class OrderedList:
	def __init__(self):
		self.head = None

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			elif current.getData() > item:
				stop = True
			else:
				current = current.getNext()

		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)

	def isEmpty(self):
		return set.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()

		return count












