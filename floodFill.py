from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib

sys.setrecursionlimit(8000)
global choice
choice = 0

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 400.0, 0, 400.0)

def readInput():
	global choice

	choice = int(input("Enter your choice: [1] Circle [2] Polygon [3] Ellipse: "))

	if choice == 1:
		global x, y, r
		x, y = map(int,raw_input("Input the centre: ").split())
		r = int(input("Input the radius of circle: "))
	
	elif choice == 2:
		global l1
		l1 = []
		n = int(input("Enter the number of sides: "))

		x0, y0 = map(int, raw_input("Input first coordinates: ").split())
		x1, y1 = map(int, raw_input("Input second coordinates: ").split())
	
		l1.append([x0 ,y0, x1, y1])
	
		temp1, temp2 = x0, y0
	
		for i in range(n-2):
			x0, y0 = x1, y1
			x1, y1 = map(int, raw_input("Input the next coordinates: ").split())
		
			l1.append([x0, y0, x1, y1])
		
	
		
		l1.append([x1, y1, temp1, temp2])
		
	elif choice == 3:
		global xc, yc, rx, ry
		
		xc, yc = map(int, raw_input("Input ellipse center: ").split())
		rx, ry = map(int, raw_input("Input major and minor axis: ").split())
	
	else:
		print "Invalid Value -- Program Exiting"
		sys.exit()

def setPixelColour(x, y, col):
    a, b, c = col[0], col[1], col[2]
    glColor3f(a, b, c)
    cglib.setPixel(x, y)

def floodFill(x, y, old, new):
	cur1 = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT, outputType = None)
	print cur1
	cur = cur1[0][0]

	print "Cur color: ", cur
	print "Old color: ", old
	flag = True
	for i in range(3):
		if old[i] != cur[i]:
			flag = False
			break
		else:
			continue
			
	if flag == True:
		setPixelColour(x, y, new)
		floodFill(x, y+1, old, new)
		floodFill(x+1, y, old, new)
		floodFill(x-1, y, old, new)
		floodFill(x, y-1, old, new)

def Mouse(button, state, x, y):
    
    print "CUR POS: ", x, y

    newColor = [[[0.0, 1.0, 0.0]]]
    oldColor = [[[0.0, 0.0, 0.0]]]

    old = oldColor[0][0]
    new = newColor[0][0]

    floodFill(x, 400-y, old, new)

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():

	glClear(GL_COLOR_BUFFER_BIT)
	global choice

	if choice == 1:
		cglib.parametricCircle(x, y, r)
	
	if choice == 2:
		global l1
		for i in range(len(l1)):
			x0, y0, x1, y1 = l1[i][0], l1[i][1], l1[i][2], l1[i][3]
			cglib.ddaLine_Simple(x0, y0, x1, y1)

	if choice == 3:
		global xc, yc, rx, ry
		cglib.midpointEllipse(xc, yc, rx, ry)


def main():
    readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(300, 200)
    glutCreateWindow("Test2")
    glutDisplayFunc(Display)
    glutMouseFunc(Mouse)

    myInit()
    glutMainLoop()

main()

# vals = glReadPixels(x, y, width?, height?, GL_RGB, GL_FLOAT?)
