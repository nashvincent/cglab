from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

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
