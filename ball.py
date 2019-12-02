from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global anim, x, y, dx, dy 

##############
def setPixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate, ycoordinate)
    glEnd()
    glFlush()

def drawCircle(xc, yc, x, y):
    setPixel(xc+x, yc+y)
    setPixel(xc-x, yc+y)
    setPixel(xc+x, yc-y)
    setPixel(xc-x, yc-y)
    setPixel(xc+y, yc+x)
    setPixel(xc-y, yc+x)
    setPixel(xc+y, yc-x)
    setPixel(xc-y, yc-x)

def bresenhamCircle(xc, yc, r):
    x, y = 0, r
    Pk = 3 - 2*r
    drawCircle(xc, yc, x, y)

    while y >= x:
        x = x + 1

        if Pk > 0:
            y = y - 1
            Pk = Pk + 4*(x-y) + 10
        
        else:
            Pk = Pk + 4*x + 6
        
        drawCircle(xc, yc, x, y)
##############

# initial position of the ball
x = 0
y = 0

# Direction vector of the ball
dx = dy = 1

# Window dimensions
width = height = 500
axrng = 25

# No animation to start
anim = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-axrng, axrng, -axrng, axrng)
    glPointSize(5.0)
    glColor3f(1.0, 0.0, 0.0)

def idle():
    # We animate only if anim == 1, otherwise
    # the ball doesn't move
    if anim == 1:
        glutPostRedisplay() 

def bounce():
    global x, y, dx, dy
    glClear(GL_COLOR_BUFFER_BIT)

    x += 0.5*dx
    y += 0.5*dy

    # Move the ball location based on x and y

    bresenhamCircle(x, y, 5)

    # Collision detection
    if x >= axrng or x <= -axrng:
        dx = -1*dx
    if y >= axrng or y <= -axrng:
        dy = -1*dy

    glFlush()

def keyboard(key, x, y):
    ''' Allows us to quit by pressing 'Esc' or 'q'
        We can animate by "a" and stop by "s"   '''

    global anim
    if key == chr(27):
        sys.exit()

    if key == "a":
        anim = 1

    if key == "s":
        anim = 0

    if key == "q":
        sys.exit()
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(width, height)
    glutCreateWindow("PyBounce")
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)

    init()
    glutMainLoop()
main() 