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
    gluOrtho2D(0, 400.0, 0, 400.0)

def readInput():
    global x, y, r, a, b
    x, y = map(int,raw_input("Input the centre: ").split())
    r = int(input("Input the radius of circle: "))
    #a, b = map(int,raw_input("Input the centre: ").split())

def setPixelColour(x, y, col):
    a, b, c = col[0], col[1], col[2]
    glColor3f(a, b, c)
    cglib.setPixel(x, y)

def floodFill(x, y, old, new):
    cur1 = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    cur = cur1[0][0]

    print "cur: ", cur
    print "Old: ", old
    flag = True
    for i in range(3):
        if old[i] != cur[i]:
            flag = False
            print "w", i
            break
    
    if flag == True:
        print "HELLO"
        setPixelColour(x, y, new)

        floodFill(x+1, y, old, new)
        floodFill(x-1, y, old, new)
        floodFill(x, y+1, old, new)
        floodFill(x, y-1, old, new)

def Mouse(button, state, x, y):
    
    print "CUR POS: ", x, y

    newColor = [[[0.0, 1.0, 0.0]]]
    oldColor = [[[0.0, 0.0, 0.0]]]

    old = oldColor[0][0]
    new = newColor[0][0]

    floodFill(x, y, old, new)

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():

    glClear(GL_COLOR_BUFFER_BIT)
    cglib.parametricCircle(x, y, r)


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