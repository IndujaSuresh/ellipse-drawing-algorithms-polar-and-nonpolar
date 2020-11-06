from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import cmath

def init():
   glClearColor(0.0,0.0,0.0,1.0)
   glColor3f(0.0,0.0,1.0)
   glPointSize(2.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(-100,100,-100,100)
   
def plot(x,y):
  glBegin(GL_POINTS)
  glVertex2f(x,y)
  glEnd()
  glFlush()
  
def uinput(): 
  glClear(GL_COLOR_BUFFER_BIT)
  
  key=int(input("Enter 1. for polar coordinates 2. for nonpolar coordinates "))
  print("Enter the x ,y ,xr ,yr : ")
  x=int(input("Enter x value:"))
  y=int(input("Enter y value:"))
  xr=int(input("Enter xr value:"))
  yr=int(input("Enter yr value:"))
  if key ==1 :
    polar(x,y,xr,yr)    
  elif key == 2:
    nonpolar(x,y,xr,yr) 
  else:
     print ("Incvalid input")
     exit   
     
def polar ( x,y,xr,yr):
    x=0
    y=yr
    angle = 0
    end_angle=(22/7)/2
    while angle <= end_angle:
        plot ( xr + x, yr + y)
        plot ( xr + x, yr- y)
        plot ( xr- x, yr - y)
        plot ( xr - x, yr + y)
        angle+=0.01
        x=(xr*math.cos(angle))
        y=(yr*math.sin(angle))
 
def nonpolar(x,y,xr,yr):
  x= (-xr)
  y=yr

  while x<0:
    y = yr * (math.sqrt(1-((x/xr)*(x/xr))))
    plot ( xr + x, yr + y)
    plot ( xr + x, yr- y)
    plot ( xr- x, yr - y)
    plot ( xr - x, yr + y)
    x+=0.01
   
def main():
   
   glutInit()
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(200,200)
   glutCreateWindow("ellipse")
   glutDisplayFunc(uinput)
   init()
    
   glutMainLoop()
 
main()
      
