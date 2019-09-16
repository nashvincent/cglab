from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib

CENTER = 0  #0000
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000 

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

def getCode(x, y):
    code = CENTER

    if x < xl:      # to the left of rectangle 
        code |= LEFT 
    elif x > xr:    # to the right of rectangle 
        code |= RIGHT

    if y < yb:      # below the rectangle 
        code |= BOTTOM 
    elif y > yt:    # above the rectangle 
        code |= TOP 
  
    return code

def clip():
    global x0, y0, x1, y1

    code1 = getCode(x0, y0)
    code2 = getCode(x1, y1)
    accept = False

    print code1

    while True:
        if code1 == 0 and code2 == 0 :
            accept = True
            break

        elif (code1 & code2) != 0:
            break

        else:
            x, y = 1, 1

            codeOut = code1 if code1 != 0 else code2

            if codeOut & TOP:
                x = x0 + ((x1-x0) / (y1-y0)) * (yt-y0)
                y = yt

            elif codeOut & BOTTOM:
                x = x0 + ((x1-x0) / (y1-y0)) * (yb-y0)
                y = yb

            elif codeOut * LEFT:
                x = xl
                y = y0 + ((y1-y0) / (x1-x0)) * (xl-x0)

            elif codeOut * RIGHT:
                x = xr
                y = y0 + ((y1-y0) / (x1-x0)) * (xr-x0)

            if codeOut == code1:
                x0 = x
                y0 = y
                code1 = getCode(x0, y0)
            
            else:
                x1 = x
                y1 = y
                code2 = getCode(x1, y1)

    if accept == False:
        x0, y0, x1, y1 = 0, 0, 0, 0

    print (x0, y0, x1, y1)
    

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    cglib.ddaLine_Simple(x0, y0, x1, y1)

def main():
    readInput()
    clip()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(300, 200)
    glutCreateWindow("Test2")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()