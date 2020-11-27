from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!") 

def display(): 
    glFlush(); 
    glColor3f(0,0.5,0.5);
    drawTriangle()
    glMatrixMode(GL_MODELVIEW);
    glTranslatef(200.0,100.0,0.0);
    glColor3f(0.5,0.0,1.0);
    drawTriangle()
    glutSwapBuffers()
    return

def drawTriangle():
    glBegin(GL_TRIANGLES);
    glVertex2f(200,200);
    glVertex2f(600,200);
    glVertex2f(400,400);
    glEnd();
 
glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB)    
glutInitWindowSize(800, 600)   
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("TRANSLATION")
#glutIdleFunc(display) 
glClearColor(0.0, 0.0, 0.0, 1.0); 
glColor3f(1.0, .5, 1.0); 
glPointSize(4.0);       
gluOrtho2D(0, 800,0, 800);
glutDisplayFunc(display)  
glutMainLoop() 
