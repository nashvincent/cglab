'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def readInput():
	global x0, y0, x1, y1,
    x0, y0 = map(int,raw_input("Input initial: ").split())
	x1, y1 = map(int,raw_input("Input final: ").split())

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	cglib.draw(x0, y0, x1, y1)

def main():
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(300, 200)
	glutCreateWindow("Test2")
	glutDisplayFunc(Display)
	myInit()
	glutMainLoop()

main()
'''