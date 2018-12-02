#-*- coding:utf-8 -*-
# Stack
# LIFO
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]	
	def size(self):
		return len(self.items)


s = Stack()

print(s.isEmpty())
s.push(3)
s.push('baby')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(9.9)
print(s.pop())
print(s.pop())
print(s.size())


# 括号对应检查
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0

	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in '([{':
			s.push(symbol)
		elif s.isEmpty():
			balanced = False
		else:
			top = s.pop()
			if not matches(top, symbol):
				balanced = False

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False


def matches(open, close):
	opens = '([{'
	closers = ')]}'
	return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


# 十进制化二进制
def divideBy2(decNumber):
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber //= 2

	binString = ''
	while not remstack.isEmpty():
		binString += str(remstack.pop())

	return binString


print(divideBy2(205))


# 十进制化八进制、十六进制
def baseConverter(decNumber, base):
	digits = '0123456789ABCDEF'

	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber //= base

	newString = ''
	while not remstack.isEmpty():
		newString += digits[remstack.pop()]

	return newString


print(baseConverter(25,8))
print(baseConverter(256,16))


# 中序遍历化后序遍历
def infixToPostfix(infixexpr):
	prec = {'*':3, '/':3, '+':2, '-':2, '(':1}
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	return ' '.join(postfixList)


# 检查后序遍历
def postfixEval(postfixexpr):
	operandStack = Stack()
	tokenList = postfixexpr.split()

	for token in tokenList:
		if token in '0123456789':
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token, operand1, operand2)
			operandStack.push(result)

	return operandStack.pop()


def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(postfixEval('7 8 + 3 2 + /'))


