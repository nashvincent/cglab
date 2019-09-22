from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

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