# Use Lists to represent a tree

myTree = ['a',  # root
		['b',  # left subtree
	   	  ['d', [], []],
	      ['e', [], []]],
	    ['c',  # right subtree
	      ['f', [], []],
	      []]
	     ]

print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])


def BinaryTree(r):
	return [r, [], []]


def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root


def getRootVal(root):
	return root[0]


def setRootVal(root, newVal):
	root[0] = newVal


def getLeftChild(root):
	return root[1]


def getRightChild(root):
	return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(l)

setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)
print(getRightChild(getRightChild(r)))


# Use nodes and references to represent a tree

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def  getRootVal(self):
		return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())


# Parse Tree

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = []
	eTree = BinaryTree('')
	pStack.append(eTree)
	currentTree = eTree

	for i in fplist:
		if i == '(':
			currentTree.insertLeft('')
			pStack.append(currentTree)
			currentTree = currentTree.getLeftChild()

		elif i not in ['+', '-', '*', '/', ')']:
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		
		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.append(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ')':
			currentTree = pStack.pop()

		else:
			raise ValueError

	return eTree


pt = buildParseTree("( ( 7 + 5 ) * 3 )")


import operator

def evaluate(parseTree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()
	print leftC

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC), evaluate(rightC))
	else:
		return parseTree.getRootVal()

print(evaluate(pt))


# Tree Traversals
def preorder(tree):
	if tree != None:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())


def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())


def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())


def postordereval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res1 = postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1, res2)
		else:
			return tree.getRootVal()


# recover the fully parenthesized version of the expression from inorderexp
def printexp(tree):
	sVal = ''
	if tree:
		sVal = '(' + printexp(tree.getLeftChild())
		sVal += str(tree.getRootVal())
		sVal += printexp(tree.getRightChild())
	return sVal


inorder(pt)
