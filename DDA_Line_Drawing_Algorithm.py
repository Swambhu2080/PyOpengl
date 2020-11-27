from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!") 
def display(): 
    glClear(GL_COLOR_BUFFER_BIT) 
    lineDDA(10, 10, 400, 400);
    glFlush();
    return
def drawDot(x, y):
    glBegin(GL_POINTS);
    glVertex2i(GLint(x),GLint(y));
    glEnd();
   
def lineDDA(x1, y1, x2, y2):
    xgap = x2 - x1;
    ygap = y2 - y1;

    if(abs(xgap) >= abs(ygap)):
        dx = xgap/abs(xgap);
        dy = ygap/abs(xgap);
        count = abs(xgap)
    else:
        dx = xgap/abs(ygap);
        dy = ygap/abs(ygap)
        count = abs(ygap)


    x = x1;
    y = y1;

    i = 1;
    while(i <= count):
        drawDot(int(x + 0.5), int(y + 0.5));
        x = x + dx;
        y = y + dy;
        i = i + 1;
 
glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB);   
glutInitWindowSize(640, 480)   
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("DDA Line Drawing Algorithm") 
glutIdleFunc(display)    
glClearColor(0.0, 0.0, 0.0, 1.0);  
glColor3f(1.0, 1.0, 1.0); 
glPointSize(4.0);         
gluOrtho2D(0, 640, 0, 480);
glutDisplayFunc(display) 
glutMainLoop()  
