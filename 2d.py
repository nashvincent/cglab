from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin, cos, pi, radians

global vertices
vertices = []

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)

def readInput():
    global vertices
	n = input('Enter number of sides: ')
	for i in range(n):
			print 'Enter coordinate: '
			x,y = map(int, raw_input().split())
			vertices.append([x,y])


def identity(r,c):
	a=[[0 for m in range(c)] for n in range(r)]
	for i in range(r):
		for j in range(c):
			if i==j:
				a[i][j]=1

	return a

def multiply(a,b):
	m=len(a)
	n=len(a[0])
	p=len(b)
	q=len(b[0])
	c=[[0 for col in range(q)] for row in range(m)]
	for i in range(m):
		for j in range(q):
			for k in range(n):
				c[i][j]+=a[i][k]*b[k][j]

	return c

def translate(tx, ty):
    global vertices

    vector = identity(3, 3)
    vector[2][0] = tx
    vector[2][1] = ty

    for i in range(len(vertices)):
        matrix = [ [vertices[i][0], vertices[i][1], 1] ]
        matrix = multiply(matrix, vector)
        vertices[i][0] = matrix[0][0]
        vertices[i][1] = matrix[0][1]

def scale(sx, sy, xr, yr):
    global vertices

    translate(-xr, -yr)
    vector = identity(3, 3)
    vector[0][0] = sx
    vector[1][1] = sy

    for i in range(len(vertices)):
        matrix = [ [vertices[i][0], vertices[i][1], 1] ]
        matrix = multiply(matrix, vector)
        vertices[i][0] = matrix[0][0]
        vertices[i][1] = matrix[0][1]

    translate(xr, yr)

def rotate(theta, xr, yr):
    global vertices

    translate(-xr, -yr)
    vector = identity(3, 3)
    thetha = radians(theta)
    vector[0][0] = round(cos(theta))
    vector[0][1] = round(-sin(theta))
    vector[1][0] = round(sin(theta))
    vector[1][1] = round(cos(theta))

    for i in range(len(vertices)):
        matrix = [ [vertices[i][0], vertices[i][1], 1] ]
        matrix = multiply(matrix, vector)
        vertices[i][0] = matrix[0][0]
        vertices[i][1] = matrix[0][1]

    translate(xr, yr)



def drawPolygon():
    print "IN"
    glClear(GL_COLOR_BUFFER_BIT)        #TODO: LOAD AXES TO MATRIX TO PRESERVE BACKGROUND

    for i in range(len(vertices)):
        glBegin(GL_LINES)
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[(i+1)%len(vertices)][0], vertices[(i+1)%len(vertices)][1])
        glEnd()
        glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    drawPolygon()

    while True:
        choice = input("Enter your choice [1]Translate [2]Rotate [3]Scale [4]Exit\n")

        if choice == 1:
            trX, trY = map(int, raw_input("Enter the translate values: ").split())
            translate(trX, trY)

        elif choice == 2:
            theta = input("Enter the angle: ")
            xr, yr = map(int, raw_input("Enter the reference points: ").split())
            rotate(theta, xr, yr)

        elif choice == 3:
            sx, sy = map(int, raw_input("Enter the scaling factors: ").split())
            xr, yr = map(int, raw_input("Enter the reference points: ").split())
            scale(sx, sy, xr, yr)

        elif choice == 4:
            sys.exit()

        drawPolygon()

def main():
    readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Test Program")
    glutDisplayFunc(draw)

    init()
    glutMainLoop()

main()
