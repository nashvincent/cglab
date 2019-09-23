from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import cglib

            #NSWE
CENTER = 0  #0000
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000

global points, flag
points = []
flag = []

def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def readInput():
    global xl ,xr, yt, yb
    xl, yb = map(int,raw_input("Input first window coordinate: ").split())
    xr, yt = map(int,raw_input("Input second window coordinate: ").split())

    n = int(input("Enter the number of lines: "))

    for i in range(n):
        x0, y0 = map(int,raw_input("Input initial: ").split())
        x1, y1 = map(int,raw_input("Input final: ").split())

        flag.append(True)
        points.append([x0, y0, x1, y1])

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

def clip(coord):

    code1 = getCode(coord[0], coord[1])
    code2 = getCode(coord[2], coord[3])
    accept = False

    print code1, code2

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
                x = coord[0] + ((coord[2]-coord[0]) / (coord[3]-coord[1])) * (yt-coord[1])
                y = yt

            elif codeOut & BOTTOM:
                x = coord[0] + ((coord[2]-coord[0]) / (coord[3]-coord[1])) * (yb-coord[1])
                y = yb

            elif codeOut * LEFT:
                x = xl
                y = coord[1] + ((coord[3]-coord[1]) / (coord[2]-coord[0])) * (xl-coord[0])

            elif codeOut * RIGHT:
                x = xr
                y = coord[1] + ((coord[3]-coord[1]) / (coord[2]-coord[0])) * (xr-coord[0])

            if codeOut == code1:
                coord[0] = x
                coord[1] = y
                code1 = getCode(coord[0], coord[1])
            
            else:
                coord[2] = x
                coord[3] = y
                code2 = getCode(coord[2], coord[3])

    if accept == False:
        return False

    return True
    

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        x1 = points[i][2]
        y1 = points[i][3]

        if flag[i] == True:
            cglib.ddaLine_Simple(x0, y0, x1, y1)
        else:
            print "\nLine clipped\n"
            

def main():
    readInput()
    for i in range(len(points)):
        flag[i] = clip(points[i])
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(300, 200)
    glutCreateWindow("Test2")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()