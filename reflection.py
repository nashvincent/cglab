'''A triangle PQR has its vertices located at P(80,50), Q(60,10),R(100,10). It is desired to
obtain its reflection about an axis parallel to Y axis and passing through poit A(30,10). Write
program do this transformation'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
global n, vertices

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)

def readInput():
    global n, vertices
    #P(80,50), Q(60,10),R(100,10)
    vertices = [[80, 50], [60, 10], [100, 10]]

def identity(row, col):
    temp = [[0 for x in range(col)] for y in range(row)]

    for i in range(row):
        for j in range(col):
            if (i == j):
                temp[i][i] = 1
    return temp

def multiply(a, b):
    m, n1 = len(a), len(a[0])
    n2, p = len(b), len(b[0])

    temp = [[0 for col in range(p)] for row in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n1):
                temp[i][j] += a[i][k] * b[k][j]
    return temp

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

def drawPolygon():
    global vertices

    for i in range(len(vertices)):
        glBegin(GL_LINES)
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[(i+1)%len(vertices)][0], vertices[(i+1)%len(vertices)][1])
        glEnd()
        glFlush()

def reflect():
    ''' To perform reflection about the Y axis '''

    vector = identity(3, 3)
    vector[0][0] = -1

    for i in range(len(vertices)):
        matrix = [ [vertices[i][0], vertices[i][1], 1] ]
        matrix = multiply(matrix, vector)

        vertices[i][0] = matrix[0][0]
        vertices[i][1] = matrix[0][1]

def draw():
    global vertices
    glClear(GL_COLOR_BUFFER_BIT)
    drawPolygon()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(30, 100)
    glVertex2f(30, -100)
    glEnd()


    translate(-30, 0)
    reflect()
    translate(30, 0)

    glColor3f(1.0, 1.0, 1.0)
    drawPolygon()

def main():
    readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Reflection")
    glutDisplayFunc(draw)

    init()
    glutMainLoop()

main()
