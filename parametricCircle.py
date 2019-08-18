from OpenGL.GL import glBegin, glVertex2i, glEnd, glFlush, GL_POINTS

def setPixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2i(xcoordinate, ycoordinate)
    glEnd()
    glFlush()

def parametricCircle(h, k, r):
	theta = 0
	STEP = 0.5

	while theta < 360:
		x = int(h + r*cos(theta))
		y = int(k + r*sin(theta))

		setPixel(x, y)
		theta = theta + STEP
