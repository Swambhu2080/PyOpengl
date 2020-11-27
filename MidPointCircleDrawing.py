from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!")

def display():
    midPointCircle(200,200,100)
    glFlush();
    glutSwapBuffers()
    return

def midPointCircle(xc,yc,radius):
    x = 0
    y = radius
    p = 1 - radius
    drawDot(x,y,(x+xc),(y+yc))
    while x <= y:
	    x += 1
	    if p < 0:
	    	p = p + 2 * x + 1
	    else:
	    	y -= 1
	    	p = p + 2 * (x - y) + 1
	    drawDot(x,y,(x+xc),(y+yc))
    
def drawDot(x, y,x1, y1):
    glBegin(GL_POINTS);
    glVertex2i(x, y);
    glVertex2i(x1, y1);
    glEnd();
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(540, 480)
glutInitWindowPosition(0, 200)
wind = glutCreateWindow("Mid Point Circle Drawing")
glClearColor(0.0, 0.0, 0.0, 1.0);
glColor3f(1.0, .5, 1.0);
glPointSize(4.0);
gluOrtho2D(0, 640, 0, 480);
glutDisplayFunc(display)
glutMainLoop()
