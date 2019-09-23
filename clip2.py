from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep
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
    global xMin, xMax, yMin, yMax
    xMin, yMin = map(int,raw_input("Input the lower window coordinates: ").split())
    xMax, yMax = map(int,raw_input("Input the upper window coordinates: ").split())

    n = int(input("Enter the number of sides of polygon: "))

def drawWindow():
    cglib.bresenhamLine(xMin, yMin, xMax, yMin)
    cglib.bresenhamLine(xMax, yMin, xMax, yMax)
    cglib.bresenhamLine(xMax, yMax, xMin, yMax)
    cglib.bresenhamLine(xMin, yMax, xMin, yMin)

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    '''
    for i in range(-250, 251):
        cglib.setPixel(i, 0)
        cglib.setPixel(0, i)
    '''

    glColor3f(0.0,1.0,0.0)

    drawWindow()

def main():
    readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("T1")
    glutDisplayFunc(Display)
    
    myInit()
    glutMainLoop()
main()
