from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!") 

def display(): 
    glClear(GL_COLOR_BUFFER_BIT) 
    bresh(10, 10, 400, 400);
    glFlush(); 
    return
    
def drawDot(x, y):
    glBegin(GL_POINTS);
    glVertex2i(GLint(x),GLint(y));
    glEnd();
 
def bresh(x1, y1, x2, y2):
    x=x1;
    y=y1;
    dx=x2-x1;
    dy=y2-y1;
    p=( (2*dy)- dx);
 
    while(x<=x2):
    	drawDot(int(x + 0.5), int(y + 0.5));
    	x=x+1
    	if(p<0):
    	  p=p+(2*dy);
    	else:
    	   p=p+(2*dy)-(2*dx);
    	   y=y+1
    	   
glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB);   
glutInitWindowSize(640, 480)  
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("Swambhu: bresenham") 
glutIdleFunc(display)    
glClearColor(0.0, 0.0, 0.0, 1.0);  
glColor3f(1.0, 1.0, 1.0); 
glPointSize(4.0);        
gluOrtho2D(0, 640, 0, 480);
glutDisplayFunc(display)  
glutMainLoop()  
