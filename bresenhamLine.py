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
    
    Pk = (2*dy) - dx

    for i in range(1, dx+1):
        setPixel(x, y)

        while Pk > 0:
            if iFlag == True:
                x = x + s1
            else:
                y = y + s2

            Pk = Pk - 2*dx
        
        if iFlag == True:
            y = y + s2
        else:
            x = x + s1

        Pk = Pk + (2*dy)
'''

def Sign(x):
	if x<0:
		return -1
	elif x==0:
		return 0
	else:
		return 1

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def bresenhamLine(x1,y1,x2,y2):
	x=x1
	y=y1
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	s1=Sign(x2-x1)
	s2=Sign(y2-y1)
	Interchange=0

	if dy>dx:
		Temp=dx
		dx=dy
		dy=Temp
		Interchange=1
	else:
		Interchange=0

	e=(2*dy)-dx

	for i in range(1,dx+1):
		setPixel(x,y)
		while e>0:
			if Interchange==1:
				x=x+s1
			else:
				y=y+s2
			e=e-(2*dx)
		if Interchange==1:
			y=y+s2
		else:
			x=x+s1
		e=e+(2*dy)

'''