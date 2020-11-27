from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
import math
import numpy as np
print("Imports successful!") 

mouseClickCount = 0
i=0
listx = []
listy = []

def display():
    global mouseClickCount, xp, yp
    glFlush(); 
    glutSwapBuffers()
    return
    
def keyPressed(*args):
    print("Event: keyPressed ")
    if args[0] == b'\x1b':
        print("Exit")
        sys.exit()
        
def mouseClicked(button, button_state, cursor_x, cursor_y):
    global mouseClickCount, xp, yp, i
    if (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
        mouseClickCount = mouseClickCount + 1
        print("mouseClickCount = ", mouseClickCount, "cursor_x = ", cursor_x, "cursor_y = ", cursor_y)
        if mouseClickCount == 1:
            glPointSize(6)
            glColor3f(0.0, 0.0, 1.0);
            drawDot(cursor_x,800-cursor_y)
            xp, yp=cursor_x, 800-cursor_y
            listx.clear()
            listy.clear()
            i=i+1
            listx.insert(i,xp)
            listy.insert(i,yp)
        elif mouseClickCount == 4:
        	glColor3f(0.0, 0.0, 1.0);
        	glPointSize(6)
        	drawDot(cursor_x,800-cursor_y)
        	drawLine(xp, yp, cursor_x, 800-cursor_y)
        	xp, yp=cursor_x, 800-cursor_y
        	i=i+1
        	listx.insert(i,xp)
        	listy.insert(i,yp)
        	mouseClickCount=0
        	bazier()
        elif mouseClickCount < 4:
        	glColor3f(0.0, 0.0, 1.0);
        	glPointSize(6)
        	drawDot(cursor_x,800-cursor_y)
        	drawLine(xp, yp, cursor_x, 800-cursor_y)
        	xp, yp=cursor_x, 800-cursor_y
        	i=i+1
        	listx.insert(i,xp)
        	listy.insert(i,yp)

def drawDot(x, y):
    #glColor3f(1.0, 0.0, 1.0);
    glBegin(GL_POINTS);
    glVertex(x,y);
    glEnd();

def drawLine(x1, y1, x2, y2):
    glColor3f(1.0, 0.0, 1.0);
    glBegin(GL_LINES);
    glVertex2i(x1, y1);
    glVertex2i(x2, y2);
    glEnd();

def bazier():
	#P = p0*B(0,3) + p1*B(1,3) + p2*B(2,3) + p3*B(3,3);
	print(listx)
	print(listy)
	for u in np.arange(0.0, 1.0, 0.001):
		x = listx[0]*math.pow((1.0-u), 3.0) + listx[1]*3.0*u*math.pow((1.0-u), 2.0) + listx[2]*(1.0-u)*3.0*math.pow(u, 2.0) + listx[3]*math.pow(u, 3.0);
		y = listy[0]*math.pow((1.0-u), 3.0) + listy[1]*3.0*u*math.pow((1.0-u), 2.0) + listy[2]*(1.0-u)*3.0*math.pow(u, 2.0) + listy[3]*math.pow(u, 3.0); 
		glColor3f(0.0, 0.9, 0.0);
		glPointSize(5)
		drawDot(x,y);

glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB);    
glutInitWindowSize(800, 800)   
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("OpenGL Coding Practice") 
glutIdleFunc(display)  
glClearColor(0.0, 0.0, 0.0, 1.0);  
glColor3f(0.0, 0.5, 0.8); 
glPointSize(4.0);        
gluOrtho2D(0, 800, 0, 800);
glutDisplayFunc(display)  
glutKeyboardFunc(keyPressed)  
glutMouseFunc(mouseClicked)
glutMainLoop()  