# Sequrntial Search
#       Case           BestCase  WorstCase  AverageCase
# item is present          1         n          n/2
# item is not present      n         n           n
# O(n)
def sequentialSearch(alist, item):
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos += 1

	return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


# Ordered Sequential Search
#       Case           BestCase  WorstCase  AverageCase
# item is present          1         n          n/2
# item is not present      1         n          n/2
# O(n)
def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False

	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		elif alist[pos] > item:
			stop = True
		else:
			pos += 1

	return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))


# Binary Search
# Comparisons	  Approximate Number of Items Left
#      1                     n/2
#      2                     n/4
#      3                     n/8
#     ...                    ...
#      i                    n/(2^i)
# O(log(n))
def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first+last)//2
		if item == alist[midpoint]:
			found = True
		elif item > alist[midpoint]:
			first = midpoint + 1
		else:
			last = midpoint - 1

	return found


def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		if item == alist[midpoint]:
			return True
		elif item > alist[midpoint]:
			return binarySearch(alist[midpoint+1:], item)
		else:
			return binarySearch(alist[:midpoint], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


# Hashing
# O(1) (concerning with load factor, λ)
# Collision Resolution:
# 	Opening addressing
# 	Rehashing
# 	Chaining

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		elif self.slots[hashvalue] == key:
			self.data[hashvalue] = data
		else:
			nextslot = self.rehash(hashvalue, len(self.slots))
			while self.slots[nextslot] != None and self.slots[nextslot] != key:
				nextslot = self.rehash(nextslot, len(self.slots))
			if self.slots[nextslot] == None:
				self.slots[nextslot] = key
				self.data[nextslot] = data
			else:
				self.data[nextslot] = data

	def hashfunction(self, key, size):
		return key%size

	def rehash(self, oldhash, size):
		return (oldhash+1)%size

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True

		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)


H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
