from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!") 

def display(): 
    glFlush();
    drawRect()
    drawTriangle()
    glMatrixMode(GL_MODELVIEW);
    #glLoadIdentity();
    glTranslatef(350.0,250.0,0.0);
    drawRect()
    drawTriangle()
    glRotatef(60.0,0.0,0.0,1.0);
    drawRect()
    drawTriangle()
    glutSwapBuffers()
    return

def drawTriangle():
    glBegin(GL_TRIANGLES);
    glColor3f(0.5,0.5,1.0);
    glVertex2f(200,300);
    glVertex2f(400,300);
    glVertex2f(300,450);
    glEnd();
    
def drawRect():
    glBegin(GL_QUADS);
    glColor3f(0.5,0.0,0.5);
    glVertex2f(200,300);#200,600
    glVertex2f(400,300);#400,600
    glVertex2f(400,150);#400,100
    glVertex2f(200,150);#200,100
    glEnd();
 
glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB)    
glutInitWindowSize(800, 800)   
glutInitWindowPosition(0, 0)  
wind = glutCreateWindow("Translation and Rotation")
#glutIdleFunc(display) 
glClearColor(0.0, 0.0, 0.0, 1.0); 
glColor3f(1.0, .5, 1.0); 
glPointSize(4.0);       
gluOrtho2D(0, 800,0, 800);
glutDisplayFunc(display)  
glutMainLoop()  