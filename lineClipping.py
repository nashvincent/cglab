from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib

def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def readInput():
    global x0, y0, x1, y1
    global xl ,xr, yt, yb

    x0, y0 = map(int,raw_input("Input initial: ").split())
    x1, y1 = map(int,raw_input("Input final: ").split())

    xl, xr = 0, 125
    yb, yt = 0, 125

def endpoint(x, y, window):
    pCode = []

    code = 1 if x < window[0] else 0
    pCode.insert(0,code) 
    code = 1 if x < window[1] else 0
    pCode.insert(0,code) 
    code = 1 if y < window[2] else 0
    pCode.insert(0,code) 
    code = 1 if y < window[3] else 0
    pCode.insert(0,code) 

    return pCode

def visible(p1, p2):
    flag = 't'

    for i in range(4):
        if p1[i] and p2[i]:
            flag = 'f'
            break

    for i in range(4):
        if p1[i] or p2[i]:
            flag = 'p'
    
    return flag

def lineClipping():
    global x0, y0, x1, y1
    global xl ,xr, yt, yb
    window = [xl ,xr, yt, yb]
    p1 = endpoint(x0, y0, window)
    p2 = endpoint(x1, y1, window)

    vFlag = visible(p1, p2)

    if vFlag == 'f':
        x0, y0, x1, y1 = 0, 0, 0, 0

    iFlag = 1

    if x0 == x1:
        iFlag = -1
    
    elif y0 == y1:
        iFlag = 0

    else:
        slope = (y1-y0) / (x1-x0)
    
    while vFlag == 'p':
        for i in range(4):
            if p1[3-i] != p2[3-i]:
                if p1[3-i] == 0:
                    x0, y0, x1, y1 = x1, y1, x0, y0
                    p1, p2 = p2, p1

                if iFlag != -1 and i <= 1:
                    y1 = slope * (window[i] - x1) + y1
                    x1 = window[i]
                    p1 = endpoint(x1, y1, window)

                if iFlag != 0 and i <= 1:
                    if iFlag != 1:
                        x1 = (1/slope) * (window[i] - y1) + x1
                    y1 = window[i]
                    p1 = endpoint(x1, y1, window)

                vFlag = visible(p1, p2)
                if vFlag == 'f':
                    x0, y0, x1, y1 = 0, 0, 0, 0

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	cglib.ddaLine_Simple(x0, y0, x1, y1)

def main():
    readInput()
    lineClipping()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(300, 200)
    glutCreateWindow("Test2")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()