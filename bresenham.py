from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def sign(a):
    if a < 0:
        return -1

    elif a == 0:
        return 0
    
    else:
        return 1

def lineBresenham(x0, y0, x1, y1):
    x = x1
    y = y1

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    s1 = sign(x1-x0)
    s2 = sign(y1-y0)
    iFlag = False

    if dy > dx:
        dx, dy = dy, dx
        iFlag = True
    
    Pk = 2*dy - dx

    for i in range(1, dx+1):
        setPixel(x, y)

        while Pk > 0:
            if iFlag:
                x = x + s1
            else:
                y = y + s2
            Pk = Pk - 2*dx
        
        if iFlag:
            y = y + s2
        else:
            x = x + s1

        Pk = Pk + 2*dy