from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Assuming homogeneous coordinates is of the from [x, y, 1]
matrix = [[1 for x in range(1)] for y in range(3)]
compositeVector = [[0 for x in range(3)] for y in range(3)]
global vertices
vertices = []

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 100, 0, 100)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    drawPolygon()
    glFlush()

def readInput():
    n = input("Enter the number of vertices: ")

    for i in range(n):
        x, y = map(int, raw_input("Enter the coordiates: ").split())
        vertices.append([x, y])

def translate(tx, ty):
    vector = [[0 for x in range(3)] for y in range(3)]
    identity(vector)
    vector[0][2] = tx
    vector[1][2] = ty
    multiply(vector, compositeVector)

def identity(m):
    for i in range(3):
        m[i][i] = 1

def drawPolygon():
    global vertices
    identity(compositeVector)
    translate(50, 50)
    
    for i in range(len(vertices)):
        matrix[0][0] = vertices[i][0]
        matrix[1][0] = vertices[i][1]

        multiply(compositeVector, matrix)
        
        vertices[i][0] = matrix[0][0]
        vertices[i][1] = matrix[1][0]

    for i in range(len(vertices) - 1):

        glBegin(GL_LINES)
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[i+1][0], vertices[i+1][1])
        glEnd()
        glFlush()

    glBegin(GL_LINES)    
    glVertex2f(vertices[i+1][0], vertices[i+1][1])
    glVertex2f(vertices[0][0], vertices[0][1])
    glEnd()

    glFlush()


def multiply(matrix_a, matrix_b):
	temp = [[0 for x in range(len(matrix_b[0]))] for y in range(len(matrix_a))]
	for i in range(len(matrix_a)):
		for j in range(len(matrix_b[0])):
			for k in range(len(matrix_a)):
				temp[i][j] += matrix_a[i][k] * matrix_b[k][j]

	for i in range(len(matrix_b)):
		for j in range(len(matrix_b[0])):
			matrix_b[i][j]=temp[i][j]

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