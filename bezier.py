from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 300, 0, 300)

def setPixel(x, y):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def readInputs():
    global pts
    pts = []

    n = int(input("Enter the number of control points: "))

    for i in range(n):
        x, y = map(int, raw_input("Enter the points: ").split())
        pts.append([x, y])

def fact(n):
    if n == 0:
        return 1

    else:
        n = n * fact(n-1)

    return n

def combination(n, r):
    return (fact(n) / (fact(r)*fact(n-r)))

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    Bezier()

def Bezier():
    l = len(pts) - 1
    count = 0.0
    
    while count <= 1.0:
        x = 0.0
        y = 0.0

        for i in range(l + 1):
            val = combination(l, i) * pow(count, i) * pow(1-count, l-i)
            x += val * pts[i][0]
            y += val * pts[i][1]

        setPixel(x, y)
        count += 0.001

def main():
    readInputs()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bezier")
    glutDisplayFunc(draw)

    init()
    glutMainLoop()

main()
