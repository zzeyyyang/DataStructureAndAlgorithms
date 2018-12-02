#-*- coding:utf-8 -*-
# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself, recursively.
def listsum(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listsum(numList[1:])


print(listsum([1, 3, 5, 7, 9]))


def fact(n):
	if n <= 1:
		return 1
	else:
		return n*fact(n-1)


print(fact(9))


# 数字化成任意进制下的字符串表示 (等价于栈操作)
def toStr(n, base):
	convertString = '0123456789ABCDEF'
	if n < base:
		return convertString[n]
	else:
		return toStr(n//base, base) + convertString[n%base]


print(toStr(769, 10))


def reverse(s):
	if len(s) <= 1:
		return s
	else:
		return s[-1] + reverse(s[:-1])


print(reverse('abcd'))


# 判断回文字符串
def removeWhite(s):
	sList = list(s)
	for i in range(len(sList)):
		if sList[i] in " ,;'":
			sList[i] = ''

	return ''.join(sList)


def isPal(s):
	if len(s) <= 1:
		return True
	else:
		return s[0] == s[-1] and isPal(s[1:-1])


print(isPal(removeWhite("x")))
print(isPal(removeWhite("radar")))
print(isPal(removeWhite("hello")))
print(isPal(removeWhite("")))
print(isPal(removeWhite("hannah")))
print(isPal(removeWhite("madam i'm adam")))


# 递归可视化
import turtle


def drawSpiral(myTurtle, lineLen):
	if lineLen > 0:
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle, lineLen-5)


myTurtle = turtle.Turtle()
myWin = turtle.Screen()
drawSpiral(myTurtle, 100)
myWin.exitonclick()


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-10,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)


t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(75,t)
myWin.exitonclick()


# 杨辉三角
import turtle


def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()


def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)


def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()


main()
