from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
print("Imports successful!") 

def display(): 
    glFlush(); 
    glColor3f(1.0, 0.5, 1.0);
    drawLine(100,150,500,150);
    drawLine(150,100,150,500);
    glColor3f(1.0, 0.0, 0.0);
    drawLine(125,250,400,400);
    glutSwapBuffers()
    return
    
def keyPressed(*args):
    print("Event: keyPressed ")
    if args[0] == b'\x1b':
        print("Exit")
        sys.exit()
        
def mouseClicked(button, button_state, cursor_x, cursor_y):
    if (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
    	drawDot(cursor_x,800-cursor_y)
        

def drawDot(x, y):
    glBegin(GL_POINTS);
    glColor3f(0.0, 0.0, 1.0);
    glVertex2i(x,y);
    glEnd();
    
def drawLine(x1, y1, x2, y2):
    glBegin(GL_LINES);
    glVertex2i(x1, y1); 
    glVertex2i(x2, y2);
    glEnd( );
 
glutInit() 
glutInitDisplayMode(GLUT_SINGLE  | GLUT_RGB);    
glutInitWindowSize(800, 800)   
glutInitWindowPosition(0, 0)   
wind = glutCreateWindow("OpenGL Coding Practice") 
glutIdleFunc(display)     
glClearColor(0.0, 0.0, 0.0,1.0); 
glPointSize(4.0);         
gluOrtho2D(0, 800, 0, 800);
glutDisplayFunc(display)  
glutKeyboardFunc(keyPressed)  
glutMouseFunc(mouseClicked)
glutMainLoop() 