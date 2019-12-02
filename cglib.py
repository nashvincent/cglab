'''
	Library function to which consists of essential output primitives to use in CG Lab
'''

from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS
from math import sin, cos

def setPixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate, ycoordinate)
    glEnd()
    glFlush()

def ddaLine_Simple(x0,y0,x1,y1):
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

def ddaLine_Symmetric(x0, y0, x1, y1):
	x, y = x0, y0
	xIncrement = x1 - x0
	yIncrement = y1 - y0

	while abs(xIncrement > 1) or abs(yIncrement > 1):
		xIncrement = xIncrement / 2.0
		yIncrement = yIncrement / 2.0

	while x < x1 or y < y1:
		setPixel(int(round(x)), int(round(y)))

		x = x + xIncrement
		y = y + yIncrement

def sign(a):
    if a < 0:
        return -1

    elif a == 0:
        return 0
    
    else:
        return 1

def bresenhamLine(x0, y0, x1, y1):
    x = x0
    y = y0

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

def parametricCircle(h, k, r):
	theta = 0
	STEP = 0.5

	while theta < 360:
		x = int(h + r*cos(theta))
		y = int(k + r*sin(theta))

		setPixel(x, y)
		theta = theta + STEP

def drawEllipse(xc, yc, x, y):
	setPixel(xc+x, yc+y)
	setPixel(xc-x, yc+y)
	setPixel(xc+x, yc-y)
	setPixel(xc-x, yc-y)

def midpointEllipse(xc, yc, rx, ry):
	x, y = 0, ry

	p1 = ry**2 - (rx**2)*ry + 0.25*(rx**2)
	dx = 2 * (ry**2) * x
	dy = 2 * (rx**2) * y

	while dx < dy:
		drawEllipse(xc, yc, x, y)

		if p1 < 0:
			x = x + 1
			dx = dx + (2 * ry**2)
			p1 = p1 + dx + ry**2

		else:
			x = x + 1
			y = y - 1
			dx = dx + (2 * ry**2)
			dy = dy - (2 * rx**2)
			p1 = p1 + dx - dy + ry**2

	p2 = ((ry**2) * ((x+0.5)**2)) + ((rx**2)*((y-1)**2)) - (rx**2)*(ry**2)

	while y >= 0:
		drawEllipse(xc, yc, x, y)

		if p2 > 0:
			y = y - 1
			dy = dy - (2*(rx**2))
			p2 = p2 + (rx**2) - dy

		else:
			y = y - 1
			x = x + 1
			dx = dx + (2*(ry**2))
			dy = dy - (2*(rx**2))
			p2 = p2 + dx - dy + (rx**2)

"""
def readInput():
    global xc, yc, rx, ry
    xc, yc = map(int,raw_input("Input center of ellipse: ").split())
    rx, ry = map(int,raw_input("Input axis of ellipse: ").split())
"""

