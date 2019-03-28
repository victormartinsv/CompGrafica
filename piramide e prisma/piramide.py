from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random

verticesTri = (
    ( 0, 1, 0),
    ( 1,-1,-1),
    (-1,-1,-1),
    (-1,-1, 1),
    ( 1,-1, 1),
    ( 1,-1,-1),
    )

verticesQuad = (
    ( 1,-1,-1),
    (-1,-1,-1),
    (-1,-1, 1),
    ( 1,-1, 1),
    )

linhasTri = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    )

linhasQuad = (
    (1,2),
    (2,3),
    (3,4),
    (4,1),
    )

coresTri = ((1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1))
coresQuad = ((0,1,0),(0,1,1),(0,0,1),(1,0,1))

def Piramideb4():
    glBegin(GL_TRIANGLE_FAN)
    for cor, v in zip(coresTri, verticesTri):
        glColor3fv(cor)
        glVertex3fv(v)
    glEnd()

    glBegin(GL_QUADS)
    for cor, v in zip(coresQuad, verticesQuad):
        glColor3fv(cor)
        glVertex3fv(v)
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    for l in linhasTri:
            for v in l:
                   glVertex3fv(verticesTri[v])
    glEnd()


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(4,1,0,0)
    Piramideb4()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE COM BASE 4")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
