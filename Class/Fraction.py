def gcd(m, n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n


class Fraction:
	def __init__(self, top, bottum):
		common = gcd(top, bottum)
		self.num = top//common
		self.den = bottum//common

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __repr__(self):
		return str(self.num) + '/' + str(self.den)

	def show(self):
		print(self.num, '/', self.den)

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def __add__(self, otherfraction):
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den*otherfraction.den
		return Fraction(newnum, newden)

	def __radd__(self, otherfraction):
		pass

	def __iadd__(self, otherfraction): # implement +=
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den*otherfraction.den
		return Fraction(newnum, newden)

	def __sub__(self, otherfraction):
		newnum = self.num*otherfraction.den - self.den*otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum, newden)

	def __mul__(self, otherfraction):
		newnum = self.num * otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum, newden)

	def __div__(self, otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num
		return Fraction(newnum, newden)

	def __eq__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum == secondnum

	def __ne__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum != secondnum

	def __gt__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum > secondnum

	def __ge__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum >= secondnum

	def __lt__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum < secondnum

	def __le__(self, otherfraction):
		firstnum = self.num * otherfraction.den
		secondnum = otherfraction.num * self.den
		return firstnum <= secondnum

x = Fraction(1,2)
y = Fraction(2,3)

print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x == y)
print(x < y)
print(x > y)

