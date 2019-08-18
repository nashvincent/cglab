from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate, ycoordinate)
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

def circleBresenham(xc, yc, r):
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