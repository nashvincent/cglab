from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib
import time

global xList, yList
xList, yList = [], []

global n

global xMin ,xMax, yMax, yMin
 
def myInit():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glColor3f(0.0, 1.0, 0.0)
	glPointSize(1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 500.0, 0, 500.0)

def readInput():
	global xMin ,xMax, yMax, yMin
	global n
	global xList, yList
	
	xMin, yMin = map(int,raw_input("Input first window coordinate: ").split())
	xMax, yMax = map(int,raw_input("Input second window coordinate: ").split())

	n = int(input("Enter the number of vertices: "))
	
	for i in range(n):
		xList.append(int(input("Enter the x coordinate: ")))
		yList.append(int(input("Enter the y coordinate: ")))
		print "\n"

'''		
def readInput():
	
	# Hardcoded in the values for testing purposes
	# Not to be used in final program

	global xMin ,xMax, yMax, yMin
	global xList, yList
	global n

	xMin, yMin = 100, 100
	xMax, yMax = 400, 400

	n = 4

	xList = [50, 250, 450, 250]
	yList = [250, 450, 250, 50]
'''	

def drawWindow():
	global xMin ,xMax, yMax, yMin
	glColor3f(0.0, 1.0, 0.0)
	cglib.bresenhamLine(xMin, yMin, xMax, yMin)
	cglib.bresenhamLine(xMax, yMin, xMax, yMax)
	cglib.bresenhamLine(xMax, yMax, xMin, yMax)
	cglib.bresenhamLine(xMin, yMax, xMin, yMin)

def clipL(x0, y0, x1, y1):
	global xnew1, ynew1

	if x1-x0 != 0:
		m = (y1-y0) / (x1-x0)
		
	else:
		m = 4000		# RANDOM VAL
		
		
	if x0 >= xMin and x1 >= xMin:				# IN -> IN
		xnew1.append(x1)
		ynew1.append(y1)
		
	elif x0 >= xMin and x1 < xMin:				# IN -> OUT
		xnew1.append(xMin)
		ynew1.append(y0 + m*(xMin - x0))
		
	elif x0 < xMin and x1 >= xMin:				# OUT -> IN
		xnew1.append(xMin)
		ynew1.append(y0 + m*(xMin - x0))
		xnew1.append(x1)
		ynew1.append(y1)

def clipR(x0, y0, x1, y1):
	global xnew2, ynew2

	if x1-x0 != 0:
		m = (y1-y0) / (x1-x0)
		
	else:
		m = 4000		# RANDOM VAL
		
		
	if x0 <= xMax and x1 <= xMax:				# IN -> IN
		xnew2.append(x1)
		ynew2.append(y1)
		
	elif x0 <= xMax and x1 > xMax:				# IN -> OUT
		xnew2.append(xMax)
		ynew2.append(y0 + m*(xMax - x0))
		
	elif x0 > xMax and x1 <= xMax:				# OUT -> IN
		xnew2.append(xMax)
		ynew2.append(y0 + m*(xMax - x0))
		xnew2.append(x1)
		ynew2.append(y1)
	
def clipB(x0, y0, x1, y1):
	global xnew1, ynew1
	
	if y1-y0 != 0:
		m = (x1-x0) / (y1-y0)
	
	else:
		m = 4000
		
	if y0 >= yMin and y1 >= yMin:				# IN -> IN
		xnew1.append(x1)
		ynew1.append(y1)
		
	elif y0 >= yMin and y1 < yMin:				# IN -> OUT
		xnew1.append(x0 + m*(yMin - y0))
		ynew1.append(yMin)
		
	elif y0 < yMin and y1 >= yMin:				# OUT -> IN
		xnew1.append(x0 + m*(yMin - y0))
		ynew1.append(yMin)
		xnew1.append(x1)
		ynew1.append(y1)
	
def clipT(x0, y0, x1, y1):
	global xnew2, ynew2
	
	if y1-y0 != 0:
		m = (x1-x0) / (y1-y0)
		
	else:
		m = 4000
		
	if y0 <= yMax and y1 <= yMax:				# IN -> IN
		xnew2.append(x1)
		ynew2.append(y1)
	
	elif y0 <= yMax and y1 > yMax:				# IN -> OUT
		xnew2.append(x0 + m*(yMax - y0))
		ynew2.append(yMax)
	
	elif y0 > yMax and y1 <= yMax:				# OUT -> IN
		xnew2.append(x0 + m*(yMax - y0))
		ynew2.append(yMax)
		xnew2.append(x1)
		ynew2.append(y1)
	
def clipPolygon():
	global xList, yList, xnew1, ynew1, xnew2, ynew2
	xnew1, ynew1, xnew2, ynew2 = [], [], [], []
	global n

	for i in range(n-1):
		clipL(xList[i], yList[i], xList[i+1], yList[i+1])
	clipL(xList[i+1], yList[i+1], xList[0], yList[0])
	
	'''	
	print "Initial" 
	print xList
	print yList
	
	print "Final"
	print xnew1
	print ynew1
	
	drawPolygon(xnew1, ynew1)
	'''
	
	for i in range(len(xnew1) - 1):
		clipR(xnew1[i], ynew1[i], xnew1[i+1], ynew1[i+1])
	clipR(xnew1[i+1], ynew1[i+1], xnew1[0], ynew1[0])
	
	'''
	print "Initial" 
	print xnew1
	print xnew1
	
	print "Final"
	print xnew2
	print ynew2
	
	drawPolygon(xnew2, ynew2)
	'''
	
	xnew1, ynew1 = [], []
	for i in range(len(xnew2) - 1):
		clipB(xnew2[i], ynew2[i], xnew2[i+1], ynew2[i+1])
	clipB(xnew2[i+1], ynew2[i+1], xnew2[0], ynew2[0])
	
	'''
	print "Initial" 
	print xnew2
	print ynew2
	
	print "Final"
	print xnew1
	print ynew1
	
	drawPolygon(xnew1, ynew1)
	'''
	
	xnew2, ynew2 = [], []
	for i in range(len(xnew1) - 1):
		clipT(xnew1[i], ynew1[i], xnew1[i+1], ynew1[i+1])
	clipT(xnew1[i+1], ynew1[i+1], xnew1[0], ynew1[0])

	print "Initial" 
	print xnew1
	print ynew1
	
	print "Final"
	print xnew2
	print ynew2
	
	drawPolygon(xnew2, ynew2)

		
def drawPolygon(xl, yl):
	glColor3f(1.0, 0.0, 0.0)

	for i in range(len(xl) - 1):
		cglib.bresenhamLine(xl[i], yl[i], xl[i+1], yl[i+1])
	cglib.bresenhamLine(xl[i+1], yl[i+1], xl[0], yl[0])

def Display():
	global xList, yList
	glClear(GL_COLOR_BUFFER_BIT)
	drawWindow()
	drawPolygon(xList, yList)
	
	time.sleep(2)
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	drawWindow()
	clipPolygon()

def main():
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(300, 200)
	glutCreateWindow("Polygon Clipping")
	glutDisplayFunc(Display)
	
	myInit()
	glutMainLoop()
	
main()


'''
Enter the x coordinate: 50
Enter the y coordinate: 250


Enter the x coordinate: 250
Enter the y coordinate: 450


Enter the x coordinate: 450
Enter the y coordinate: 250


Enter the x coordinate: 250
Enter the y coordinate: 50

'''
