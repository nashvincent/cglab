from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def lineDDA(x0,y0,x1,y1):
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    x, y = x0, y0
    steps = dx if dx > dy else dy
    
    xIncrement = (x1-x0)/float(steps)
    yIncrement = (y1-y0)/float(steps)
    setPixel(int(round(x)), int(round(y)))

    for k in range(steps):
        x+= xIncrement
        y+= yIncrement
        setPixel(int(round(x)), int(round(y)))  
