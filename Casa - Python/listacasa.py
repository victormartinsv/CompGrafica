from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
window = 0
xrot = yrot = zrot = 0.0
dx = 0
dy = 0.1
dz = 0

def LoadTextures():
    global texture
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(8)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='frenteCasa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='fundoscasa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='telhado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[3])
    reader = png.Reader(filename='chao.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[4])
    reader = png.Reader(filename='portasjanelas.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[5])
    reader = png.Reader(filename='grafite.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    glDisable(GL_TEXTURE_2D)

def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

id_casa = -1
id_mundo = -1
def CriarMundo():
	global id_mundo
	id_mundo = glGenLists(1)
        glNewList(id_mundo, GL_COMPILE_AND_EXECUTE)
        glFrontFace(GL_CCW)
	glBegin(GL_QUADS)
	#ceufundo
        glColor3f(0,0,1); glVertex3f(20.0,10.0,-10.0)
        glColor3f(0,0,1);  glVertex3f(-20.0,10.0,-10.0)
        glColor3f(0.5,0.8,1); glVertex3f(-20.0,-5.0,-10.0)
        glColor3f(0.5,0.8,1); glVertex3f(20.0,-5.0,-10.0)
    	#fundosuperior
    	glColor3f(0,0,0); glVertex3f(20.0,20.0,-10.0)
    	glColor3f(0,0,0);  glVertex3f(-20.0,20.0,-10.0)
    	glColor3f(0,0,1); glVertex3f(-20.0,10.0,-10.0)
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,-10.0)
    	#ceudireita
    	glColor3f(0,0,1); glVertex3f(-20.0,10.0,-10.0)
    	glColor3f(0,0,1);  glVertex3f(-20.0,10.0,14.0)
   	glColor3f(0.5,0.8,1); glVertex3f(-20.0,-5.0,14.0)
    	glColor3f(0.5,0.8,1); glVertex3f(-20.0,-5.0,-14.0)
    	#direitasuperior
    	glColor3f(0,0,0); glVertex3f(-20.0,20.0,-10.0)
    	glColor3f(0,0,0);  glVertex3f(-20.0,20.0,14.0)
    	glColor3f(0,0,1); glVertex3f(-20.0,10.0,14.0)
    	glColor3f(0,0,1); glVertex3f(-20.0,10.0,-10.0)
    	#ceuesquerda
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,14.0)
    	glColor3f(0,0,1);  glVertex3f(20.0,10.0,-10.0)
    	glColor3f(0.5,0.8,1); glVertex3f(20.0,-5.0,-10.0)
    	glColor3f(0.5,0.8,1); glVertex3f(20.0,-5.0,14.0)
    	#esquerdasuperior
    	glColor3f(0,0,0); glVertex3f(20.0,20.0,14.0)
    	glColor3f(0,0,0);  glVertex3f(20.0,20.0,-10.0)
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,-10.0)
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,14.0)
    	#ceufrente
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,14.0)
    	glColor3f(0,0,1);  glVertex3f(-20.0,10.0,14.0)
    	glColor3f(0.5,0.8,1); glVertex3f(-20.0,-5.0,14.0)
    	glColor3f(0.5,0.8,1); glVertex3f(20.0,-5.0,14.0)
    	#frentesupeior
    	glColor3f(0,0,0); glVertex3f(20.0,20.0,14.0)
    	glColor3f(0,0,0);  glVertex3f(-20.0,20.0,14.0)
    	glColor3f(0,0,1); glVertex3f(-20.0,10.0,14.0)
    	glColor3f(0,0,1); glVertex3f(20.0,10.0,14.0)
    	glEnd()
    	glBegin(GL_QUADS)
    	#ruaPrincipal1
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f(-20.0, -1.0,  2.5)
    	glVertex3f( 20.0, -1.0,  2.5)
    	glVertex3f( 20.0, -1.0,  5.5)
    	glVertex3f(-20.0, -1.0,  5.5)
    	#ruaPrincipal2
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f(-20.0, -1.0, -6.01)
    	glVertex3f( 20.0, -1.0, -6.01)
    	glVertex3f( 20.0, -1.0, -3.0)
    	glVertex3f(-20.0, -1.0, -3.0)
    	#ruaPrincipal3
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f(-20.0, -1.0, 14.0)
    	glVertex3f( 20.0, -1.0, 14.0)
    	glVertex3f( 20.0, -1.0, 11.0)
        glVertex3f(-20.0, -1.0, 11.0)
    #faixasRuaPrincipal1
        glColor3f(1,1,0)
        glVertex3f(-18.0, -0.99, 3.9)
        glVertex3f(-16.0, -0.99, 3.9)
        glVertex3f(-16.0, -0.99, 4.1)
        glVertex3f(-18.0, -0.99, 4.1)

        glVertex3f(-14.0, -0.99, 3.9)
        glVertex3f(-12.0, -0.99, 3.9)
        glVertex3f(-12.0, -0.99, 4.1)
        glVertex3f(-14.0, -0.99, 4.1)

        glVertex3f(-10.0, -0.99, 3.9)
        glVertex3f( -8.0, -0.99, 3.9)
        glVertex3f( -8.0, -0.99, 4.1)
        glVertex3f(-10.0, -0.99, 4.1)

        glVertex3f(-6.0, -0.99, 3.9)
        glVertex3f(-4.0, -0.99, 3.9)
        glVertex3f(-4.0, -0.99, 4.1)
        glVertex3f(-6.0, -0.99, 4.1)

        glVertex3f(-2.0, -0.99, 3.9)
        glVertex3f( 0.0, -0.99, 3.9)
        glVertex3f( 0.0, -0.99, 4.1)
        glVertex3f(-2.0, -0.99, 4.1)

        glVertex3f( 2.0, -0.99, 3.9)
        glVertex3f( 4.0, -0.99, 3.9)
        glVertex3f( 4.0, -0.99, 4.1)
        glVertex3f( 2.0, -0.99, 4.1)

        glVertex3f( 6.0, -0.99, 3.9)
        glVertex3f( 8.0, -0.99, 3.9)
        glVertex3f( 8.0, -0.99, 4.1)
        glVertex3f( 6.0, -0.99, 4.1)

        glVertex3f( 10.0, -0.99, 3.9)
        glVertex3f( 12.0, -0.99, 3.9)
        glVertex3f( 12.0, -0.99, 4.1)
        glVertex3f( 10.0, -0.99, 4.1)

        glVertex3f( 14.0, -0.99, 3.9)
        glVertex3f( 16.0, -0.99, 3.9)
        glVertex3f( 16.0, -0.99, 4.1)
        glVertex3f( 14.0, -0.99, 4.1)

        glVertex3f( 18.0, -0.99, 3.9)
        glVertex3f( 20.0, -0.99, 3.9)
        glVertex3f( 20.0, -0.99, 4.1)
        glVertex3f( 18.0, -0.99, 4.1)

        #faixasRuaPrincipal2
        glColor3f(1,1,0)
        glVertex3f(-18.0, -0.99, -4.4)
        glVertex3f(-16.0, -0.99, -4.4)
        glVertex3f(-16.0, -0.99, -4.6)
        glVertex3f(-18.0, -0.99, -4.6)

        glVertex3f(-14.0, -0.99, -4.4)
        glVertex3f(-12.0, -0.99, -4.4)
        glVertex3f(-12.0, -0.99, -4.6)
        glVertex3f(-14.0, -0.99, -4.6)

        glVertex3f(-10.0, -0.99, -4.4)
        glVertex3f( -8.0, -0.99, -4.4)
        glVertex3f( -8.0, -0.99, -4.6)
        glVertex3f(-10.0, -0.99, -4.6)

        glVertex3f(-6.0, -0.99, -4.4)
        glVertex3f(-4.0, -0.99, -4.4)
        glVertex3f(-4.0, -0.99, -4.6)
        glVertex3f(-6.0, -0.99, -4.6)

        glVertex3f(-2.0, -0.99, -4.4)
        glVertex3f( 0.0, -0.99, -4.4)
        glVertex3f( 0.0, -0.99, -4.6)
        glVertex3f(-2.0, -0.99, -4.6)

        glVertex3f( 2.0, -0.99, -4.4)
        glVertex3f( 4.0, -0.99, -4.4)
        glVertex3f( 4.0, -0.99, -4.6)
        glVertex3f( 2.0, -0.99, -4.6)

        glVertex3f( 6.0, -0.99, -4.4)
        glVertex3f( 8.0, -0.99, -4.4)
        glVertex3f( 8.0, -0.99, -4.6)
        glVertex3f( 6.0, -0.99, -4.6)

        glVertex3f( 10.0, -0.99, -4.4)
        glVertex3f( 12.0, -0.99, -4.4)
        glVertex3f( 12.0, -0.99, -4.6)
        glVertex3f( 10.0, -0.99, -4.6)

        glVertex3f( 14.0, -0.99, -4.4)
        glVertex3f( 16.0, -0.99, -4.4)
        glVertex3f( 16.0, -0.99, -4.6)
        glVertex3f( 14.0, -0.99, -4.6)

        glVertex3f( 18.0, -0.99, -4.4)
        glVertex3f( 20.0, -0.99, -4.4)
        glVertex3f( 20.0, -0.99, -4.6)
        glVertex3f( 18.0, -0.99, -4.6)

        #faixasRuaPrincipal3
        glColor3f(1,1,0)
        glVertex3f(-18.0, -0.99, 12.4)
        glVertex3f(-16.0, -0.99, 12.4)
        glVertex3f(-16.0, -0.99, 12.6)
        glVertex3f(-18.0, -0.99, 12.6)

        glVertex3f(-14.0, -0.99, 12.4)
        glVertex3f(-12.0, -0.99, 12.4)
        glVertex3f(-12.0, -0.99, 12.6)
        glVertex3f(-14.0, -0.99, 12.6)

        glVertex3f(-10.0, -0.99, 12.4)
        glVertex3f( -8.0, -0.99, 12.4)
        glVertex3f( -8.0, -0.99, 12.6)
        glVertex3f(-10.0, -0.99, 12.6)

        glVertex3f(-6.0, -0.99, 12.4)
        glVertex3f(-4.0, -0.99, 12.4)
        glVertex3f(-4.0, -0.99, 12.6)
        glVertex3f(-6.0, -0.99, 12.6)

        glVertex3f(-2.0, -0.99, 12.4)
        glVertex3f( 0.0, -0.99, 12.4)
        glVertex3f( 0.0, -0.99, 12.6)
        glVertex3f(-2.0, -0.99, 12.6)

        glVertex3f( 2.0, -0.99, 12.4)
        glVertex3f( 4.0, -0.99, 12.4)
        glVertex3f( 4.0, -0.99, 12.6)
        glVertex3f( 2.0, -0.99, 12.6)

        glVertex3f( 6.0, -0.99, 12.4)
        glVertex3f( 8.0, -0.99, 12.4)
        glVertex3f( 8.0, -0.99, 12.6)
        glVertex3f( 6.0, -0.99, 12.6)

        glVertex3f( 10.0, -0.99, 12.4)
        glVertex3f( 12.0, -0.99, 12.4)
        glVertex3f( 12.0, -0.99, 12.6)
        glVertex3f( 10.0, -0.99, 12.6)

        glVertex3f( 14.0, -0.99, 12.4)
        glVertex3f( 16.0, -0.99, 12.4)
        glVertex3f( 16.0, -0.99, 12.6)
        glVertex3f( 14.0, -0.99, 12.6)

        glVertex3f( 18.0, -0.99, 12.4)
        glVertex3f( 20.0, -0.99, 12.4)
        glVertex3f( 20.0, -0.99, 12.6)
        glVertex3f( 18.0, -0.99, 12.6)

    	#ruaTransversal1
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f( 3.0, -1.0,  14.0)
    	glVertex3f( 5.0, -1.0,  14.0)
    	glVertex3f( 5.0, -1.0,  -6.01)
    	glVertex3f( 3.0, -1.0,  -6.01)
    	#ruaTransversal2
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f( -3.0, -1.0,  14.0)
    	glVertex3f( -5.0, -1.0,  14.0)
    	glVertex3f( -5.0, -1.0,  -6.01)
    	glVertex3f( -3.0, -1.0,  -6.01)
    	#ruaTransversal3
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f( 11.0, -1.0,  14.0)
    	glVertex3f( 13.0, -1.0,  14.0)
    	glVertex3f( 13.0, -1.0,  -6.01)
    	glVertex3f( 11.0, -1.0,  -6.01)
    	#ruaTransversal4
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f( 19.0, -1.0,  14.0)
    	glVertex3f( 20.0, -1.0,  14.0)
    	glVertex3f( 20.0, -1.0,  -6.01)
    	glVertex3f( 19.0, -1.0,  -6.01)
    	#ruaTransversal5
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f(-11.0, -1.0,  14.0)
    	glVertex3f(-13.0, -1.0,  14.0)
    	glVertex3f(-13.0, -1.0,  -6.01)
    	glVertex3f(-11.0, -1.0,  -6.01)
    	#ruaTransversal6
    	glColor3f(0.5,0.5,0.5)
    	glVertex3f(-19.0, -1.0,  14.0)
    	glVertex3f(-20.0, -1.0,  14.0)
    	glVertex3f(-20.0, -1.0,  -6.01)
    	glVertex3f(-19.0, -1.0,  -6.01)
    	glEnd()
    	#muro
    	glBegin(GL_QUADS)
    	glColor3f(0,0,1)
    	glVertex3f(-20.0, -1.0,  -6.01)
    	glVertex3f( 20.0, -1.0,  -6.01)
    	glVertex3f( 20.0, 1.0,  -6.01)
    	glVertex3f(-20.0, 1.0,  -6.01)
	glEnd()
        glBindTexture(GL_TEXTURE_2D, texture[5])
	glBegin(GL_QUADS)
    	glTexCoord2f(1,1);	glVertex3f(19.99, -1.0,  4.0)
    	glTexCoord2f(0,1);	glVertex3f(19.99, -1.0,  -6.01)
        glTexCoord2f(0,0);	glVertex3f(19.99, 1.0,  -6.01)
    	glTexCoord2f(1,0);	glVertex3f(19.99, 1.0,  4.0)
	glEnd()
#    	glVertex3f(19.99, -1.0,  4.0)
#    	glVertex3f(19.99, -1.0,  14.0)
#    	glVertex3f(19.99, 1.0,  14.0)
#        glVertex3f(19.99, 1.0,  4.0)

	glBegin(GL_QUADS)
    	glColor3f(1,1,0)
    	glVertex3f(-19.99, -1.0,  -6.01)
    	glVertex3f(-19.99, -1.0,  14.0)
    	glVertex3f(-19.99, 1.0,  14.0)
    	glVertex3f(-19.99, 1.0,  -6.01)
    	glColor3f(0,0,1)
    	glVertex3f(-20.0, -1.0,  13.99)
    	glVertex3f( 20.0, -1.0, 13.99)
    	glVertex3f( 20.0, 1.0,  13.99)
    	glVertex3f(-20.0, 1.0,  13.99)
    	glEnd()
    	#chao
    	glBegin(GL_QUADS)
    	glColor3f(0.5,1.0,0.0)

    	glVertex3f(-20.0, -1.001,  14.0)
    	glVertex3f( 20.0, -1.001,  14.0)
    	glVertex3f( 20.0, -1.001, -6.01)
    	glVertex3f(-20.0, -1.001, -6.01)

    	glVertex3f(-20.0, -9.000,  14.0)
    	glVertex3f(-20.0, -1.001,  14.0)
    	glVertex3f( 20.0, -1.001,  14.0)
    	glVertex3f( 20.0, -9.000,  14.0)

    	glVertex3f(-20.0, -9.000,  -6.01)
    	glVertex3f(-20.0, -1.001,  -6.01)
    	glVertex3f( 20.0, -1.001,  -6.01)
    	glVertex3f( 20.0, -9.000,  -6.01)

    	glVertex3f( 20.0, -9.000,   14.0)
    	glVertex3f( 20.0, -1.001,   14.0)
    	glVertex3f( 20.0, -1.001,  -6.01)
    	glVertex3f( 20.0, -9.000,  -6.01)

    	glVertex3f(-20.0, -9.000,   14.0)
    	glVertex3f(-20.0, -1.001,   14.0)
    	glVertex3f(-20.0, -1.001,  -6.01)
    	glVertex3f(-20.0, -9.000,  -6.01)
    	glEnd()
	glEndList()

def CriarCasa():
	global id_casa
	id_casa = glGenLists(1)
        glNewList(id_casa, GL_COMPILE)
        glFrontFace(GL_CCW)
	glEnable(GL_TEXTURE_2D)
	glBindTexture(GL_TEXTURE_2D, texture[0])
        #frente3
    	glBegin(GL_QUADS)
    	glTexCoord2f(0.1136, 0.77); glVertex3f(-0.24, -1.0,  1.2)
    	glTexCoord2f(0.1136, 0.37); glVertex3f(-0.24,  0.5,  1.2)
    	glTexCoord2f(0.5, 0.37);  glVertex3f( 1.50,  0.5,  1.2)
    	glTexCoord2f(0.5, 0.77);  glVertex3f( 1.50, -1.0,  1.2)
    	glEnd()
    	glBegin(GL_TRIANGLES)
    	glTexCoord2f(0.1136, 0.37); glVertex3f(-0.24,  0.5,  1.2)
    	glTexCoord2f(0.307, 0.09);  glVertex3f(0.60,  1.3,  1.2)
    	glTexCoord2f(0.5, 0.37);  glVertex3f(1.50,  0.5,  1.2)
    	glEnd()
        #lateralDireita3
    	glBegin(GL_QUADS)
    	glTexCoord2f(0.5, 0.77);   glVertex3f( 1.50, -1.0, -1.3)
    	glTexCoord2f(0.5, 0.37);   glVertex3f( 1.50,  0.5, -1.3)
    	glTexCoord2f(0.89, 0.37);  glVertex3f(1.50, 0.5, 1.2)
    	glTexCoord2f(0.89, 0.77);  glVertex3f(1.50,-1.0, 1.2)
	glEnd()
        glBindTexture(GL_TEXTURE_2D, texture[1])
        #fundos3
    	glBegin(GL_QUADS)
    	glTexCoord2f(0.1136, 0.75); glVertex3f(-0.24, -1.0,  -1.3)
    	glTexCoord2f(0.1136, 0.37); glVertex3f(-0.24,  0.5,  -1.3)
    	glTexCoord2f(0.5, 0.37);  glVertex3f( 1.50,  0.5,  -1.3)
    	glTexCoord2f(0.5, 0.75);  glVertex3f( 1.50, -1.0,  -1.3)
    	glEnd()
    	glBegin(GL_TRIANGLES)
    	glTexCoord2f(0.1136, 0.37); glVertex3f(-0.24,  0.5,  -1.3)
    	glTexCoord2f(0.307, 0.09);  glVertex3f(0.60,  1.3,  -1.3)
    	glTexCoord2f(0.5, 0.37);  glVertex3f(1.50,  0.5,  -1.3)
    	glEnd()
	#lateralEsquerda3
    	glBegin(GL_QUADS)
    	glTexCoord2f(0.5, 0.761);  glVertex3f(-0.24, -1.0, -1.3)
    	glTexCoord2f(0.886, 0.761);  glVertex3f(-0.24, -1.0,  1.2)
    	glTexCoord2f(0.886, 0.37); glVertex3f(-0.24,  0.5,  1.2)
    	glTexCoord2f(0.5, 0.37); glVertex3f(-0.24,  0.5, -1.3)
	glEnd()
     	glBindTexture(GL_TEXTURE_2D, texture[2])
   	glBegin(GL_QUAD_STRIP)
	#telhado3
    	glTexCoord2f(0.49, 0.165);  glVertex3f(1.60,  0.45,  1.28)
    	glTexCoord2f(0.49, 0.765);  glVertex3f(1.60,  0.45, -1.38)
    	glTexCoord2f(0.19, 0.165);  glVertex3f(0.60,  1.3,  1.28)
    	glTexCoord2f(0.19, 0.765);  glVertex3f(0.60,  1.3, -1.38)
    	glTexCoord2f(0.79, 0.165);  glVertex3f(-0.34,  0.45, 1.28)
    	glTexCoord2f(0.79, 0.765);  glVertex3f(-0.34,  0.45, -1.38)
    	glEnd()
    	glBindTexture(GL_TEXTURE_2D, texture[3])
   	glBegin(GL_QUADS)
        #chao3
    	glTexCoord2f(0.045, 0.92);   glVertex3f(-2.0, -1.0,  2.0)
    	glTexCoord2f(0.94, 0.92);  glVertex3f( 2.0, -1.0,  2.0)
    	glTexCoord2f(0.94, 0.025);  glVertex3f( 2.0, -1.0, -2.0)
    	glTexCoord2f(0.045, 0.025);  glVertex3f(-2.0, -1.0, -2.0)
    	#calcadaruaprincipalcasa3
    	glTexCoord2f(0.08, 0.16);   glVertex3f(-3.0, -0.9999,  2.5)
    	glTexCoord2f(0.08, 0.92);  glVertex3f( 3.0, -0.9999,  2.5)
    	glTexCoord2f(0.38, 0.92);  glVertex3f( 3.0, -0.9999, 2.0)
    	glTexCoord2f(0.38, 0.16);  glVertex3f(-3.0, -0.9999, 2.0)
	#calcadaruaprincipaloposto3
    	glTexCoord2f(0.08, 0.16);   glVertex3f(-3.0, -0.9999,  6.0)
    	glTexCoord2f(0.08, 0.92);  glVertex3f( 3.0, -0.9999,  6.0)
    	glTexCoord2f(0.38, 0.92);  glVertex3f( 3.0, -0.9999, 5.5)
    	glTexCoord2f(0.38, 0.16);  glVertex3f(-3.0, -0.9999, 5.5)
    	#calcadaLateralesquerda3
    	glTexCoord2f(0.08, 0.16);   glVertex3f(-3.0, -0.9999,  2.0)
    	glTexCoord2f(0.38, 0.16);  glVertex3f(-2.0, -0.9999,  2.0)
    	glTexCoord2f(0.38, 0.92);  glVertex3f(-2.0, -0.9999, -2.0)
    	glTexCoord2f(0.08, 0.92);  glVertex3f(-3.0, -0.9999, -2.0)
    	#calcadaLateraldireita3
    	glTexCoord2f(0.08, 0.16);   glVertex3f(3.0, -0.9999,  2.0)
    	glTexCoord2f(0.38, 0.16);  glVertex3f(2.0, -0.9999,  2.0)
    	glTexCoord2f(0.38, 0.92);  glVertex3f(2.0, -0.9999, -2.0)
    	glTexCoord2f(0.08, 0.92);  glVertex3f(3.0, -0.9999, -2.0)
    	#calcadaFundos3
    	glTexCoord2f(0.08, 0.16);   glVertex3f(-3.0, -0.9999, -2.0)
    	glTexCoord2f(0.08, 0.92);  glVertex3f( 3.0, -0.9999,  -2.0)
    	glTexCoord2f(0.38, 0.92);  glVertex3f( 3.0, -0.9999, -3.0)
    	glTexCoord2f(0.38, 0.16);  glVertex3f(-3.0, -0.9999, -3.0)
	glEnd()
	glBindTexture(GL_TEXTURE_2D, texture[4])
    	glBegin(GL_QUADS)
        #porta3
     	glTexCoord2f(0.85, 0.79); glVertex3f(0.83, -0.95,  1.201)
     	glTexCoord2f(0.85, 0.56); glVertex3f(0.83, -0.08,  1.201)
   	glTexCoord2f(0.94, 0.56);  glVertex3f( 1.29,  -0.08,  1.201)
    	glTexCoord2f(0.94, 0.79);  glVertex3f( 1.29, -0.95,  1.201)
    	#janelafrontal3
    	glTexCoord2f(0.54, 0.78); glVertex3f(0.055, -0.70,  1.201)
    	glTexCoord2f(0.54, 0.638); glVertex3f(0.055, -0.078,  1.201)
    	glTexCoord2f(0.608, 0.638);  glVertex3f(0.36, -0.078,  1.201)
    	glTexCoord2f(0.608, 0.78);  glVertex3f(0.36, -0.70,  1.201)
    	#janeladireita3
    	glTexCoord2f(0.54, 0.78); glVertex3f(1.501, -0.69,  0.278)
    	glTexCoord2f(0.54, 0.638); glVertex3f(1.501, -0.05,  0.278)
    	glTexCoord2f(0.608, 0.638);  glVertex3f(1.501, -0.05,  -0.27)
    	glTexCoord2f(0.608, 0.78);  glVertex3f(1.501, -0.69,  -0.27)
        #janelaesquerda3
    	glTexCoord2f(0.055, 0.77); glVertex3f(-0.241, -0.66,  0.69)
    	glTexCoord2f(0.055, 0.62); glVertex3f(-0.241, -0.062,  0.69)
    	glTexCoord2f(0.1865, 0.62);  glVertex3f(-0.241, -0.062,  -0.27)
    	glTexCoord2f(0.1865, 0.77);  glVertex3f(-0.241, -0.66,  -0.27)
        #janelafundos3
    	glTexCoord2f(0.54, 0.78); glVertex3f(0.055, -0.69,  -1.301)
    	glTexCoord2f(0.54, 0.638); glVertex3f(0.055, -0.078,  -1.301)
    	glTexCoord2f(0.608, 0.638);  glVertex3f(0.38, -0.078,  -1.301)
    	glTexCoord2f(0.608, 0.78);  glVertex3f(0.38, -0.69,  -1.301)
    	#janelafrontalsuperior3
    	glTexCoord2f(0.275, 0.74);  glVertex3f(0.53, 0.7, 1.201)
    	glTexCoord2f(0.275, 0.66);  glVertex3f(0.53, 0.95, 1.201)
    	glTexCoord2f(0.31, 0.66);  glVertex3f(0.72, 0.95, 1.201)
    	glTexCoord2f(0.31, 0.74);  glVertex3f(0.72, 0.7, 1.201)
   	#chamine3
    	#lateralEsquerda
    	glTexCoord2f(0.848, 0.39); glVertex3f(-0.20, 0.50, -1.22)
    	glTexCoord2f(0.848, 0.21); glVertex3f(-0.20, 1.1, -1.22)
    	glTexCoord2f(0.90, 0.21);  glVertex3f(-0.20, 1.1, -0.85)
    	glTexCoord2f(0.90, 0.39);  glVertex3f(-0.20, 0.50, -0.85)
    	#lateraldireta
    	glTexCoord2f(0.848, 0.39); glVertex3f(0.095, 0.50, -1.22)
    	glTexCoord2f(0.848, 0.21); glVertex3f(0.095, 1.1, -1.22)
    	glTexCoord2f(0.90, 0.21);  glVertex3f(0.095, 1.1, -0.85)
    	glTexCoord2f(0.90, 0.39);  glVertex3f(0.095, 0.50, -0.85)
    	#frente
    	glTexCoord2f(0.848, 0.39); glVertex3f(-0.20, 0.50, -0.85)
    	glTexCoord2f(0.848, 0.21); glVertex3f(-0.20, 1.1, -0.85)
    	glTexCoord2f(0.90, 0.21);  glVertex3f(0.095, 1.1, -0.85)
    	glTexCoord2f(0.90, 0.39);  glVertex3f(0.095, 0.50, -0.85)
    	#fundo
    	glTexCoord2f(0.848, 0.39); glVertex3f(-0.20, 0.50, -1.22)
    	glTexCoord2f(0.848, 0.21); glVertex3f(-0.20, 1.1, -1.22)
    	glTexCoord2f(0.90, 0.21);  glVertex3f(0.095, 1.1, -1.22)
    	glTexCoord2f(0.90, 0.39);  glVertex3f(0.095, 0.50, -1.22)
    	#cima
    	glTexCoord2f(0.848, 0.20); glVertex3f(-0.20, 1.1, -0.85)
    	glTexCoord2f(0.848, 0.13); glVertex3f(-0.20, 1.1, -1.22)
    	glTexCoord2f(0.90, 0.13);  glVertex3f(0.095, 1.1, -1.22)
	glEnd()
    	#murogrande
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.06, 0.38); glVertex3f(-0.40, -1.0, 2.0)
    	glTexCoord2f(0.06, 0.25); glVertex3f(-0.40, -0.70, 2.0)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(0.75, -0.70, 2.0)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(0.75, -1.0, 2.0)
    	#murofundo
    	glTexCoord2f(0.06, 0.38); glVertex3f(-0.40, -1.0, 1.7)
    	glTexCoord2f(0.06, 0.25); glVertex3f(-0.40, -0.70, 1.7)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(0.75, -0.70, 1.7)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(0.75, -1.0, 1.7)
    	#murocima
    	glTexCoord2f(0.09, 0.24); glVertex3f(-0.40, -0.70, 2.0)
    	glTexCoord2f(0.09, 0.203); glVertex3f(-0.40, -0.70, 1.7)
    	glTexCoord2f(0.2, 0.203);  glVertex3f(0.75, -0.70, 1.7)
    	glTexCoord2f(0.2, 0.24);  glVertex3f(0.75, -0.70, 2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(-0.40, -1.0, 2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(-0.40, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(-0.40, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(-0.40,-1.0, 1.7)
    	#muroesquerda
    	glTexCoord2f(0.30, 0.38);   glVertex3f(0.75, -1.0, 2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(0.75, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(0.75, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(0.75, -1.0, 1.7)
    	glEnd()
    	#muropequeno
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.06, 0.38); glVertex3f(1.40, -1.0, 2.0)
    	glTexCoord2f(0.06, 0.25); glVertex3f(1.40, -0.70, 2.0)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(2.0, -0.70, 2.0)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(2.0, -1.0, 2.0)
    	#murofundo
    	glTexCoord2f(0.06, 0.38); glVertex3f(1.40, -1.0, 1.7)
    	glTexCoord2f(0.06, 0.25); glVertex3f(1.40, -0.70, 1.7)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(2.0, -0.70, 1.7)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(2.0, -1.0, 1.7)
    	#murocima
    	glTexCoord2f(0.09, 0.24); glVertex3f(1.40, -0.70, 2.0)
    	glTexCoord2f(0.09, 0.203); glVertex3f(1.40, -0.70, 1.7)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(2.0, -0.70, 1.7)
    	glTexCoord2f(0.20, 0.24);  glVertex3f(2.0, -0.70, 2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(1.40, -1.0, 2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(1.40, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(1.40, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(1.40,-1.0, 1.7)
    	#muroesquerda
    	glTexCoord2f(0.30, 0.38);   glVertex3f(2.0, -1.0, 2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(2.0, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(2.0, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(2.0, -1.0, 1.7)
    	glEnd()
    	#murograndefundos
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.068, 0.38); glVertex3f(0.0, -1.0, -2.0)
    	glTexCoord2f(0.068, 0.25); glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(2.0, -0.70, -2.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(2.0, -1.0, -2.0)
    	#murofundo
    	glTexCoord2f(0.068, 0.38); glVertex3f(0.0, -1.0, -1.7)
    	glTexCoord2f(0.068, 0.25); glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(2.0, -0.70, -1.7)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(2.0, -1.0, -1.7)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.068, 0.203); glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(2.0, -0.70, -1.7)
    	glTexCoord2f(0.20, 0.24);  glVertex3f(2.0, -0.70, -2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(0.0, -1.0, -2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(0.0,-1.0, -1.7)
    	#muroesquerda
    	glTexCoord2f(0.30, 0.38);   glVertex3f(2.0, -1.0, -2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(2.0, -0.70, -2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(2.0, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(2.0, -1.0, -1.7)
    	glEnd()
    	#murograndefundos
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.06, 0.38); glVertex3f(0.0, -1.0, -2.0)
   	glTexCoord2f(0.06, 0.25); glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(-2.0, -0.70, -2.0)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(-2.0, -1.0, -2.0)
    	#murofundo
    	glTexCoord2f(0.06, 0.38); glVertex3f(0.0, -1.0, -1.7)
    	glTexCoord2f(0.06, 0.25); glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.30, 0.25);  glVertex3f(-2.0, -0.70, -1.7)
    	glTexCoord2f(0.30, 0.38);  glVertex3f(-2.0, -1.0, -1.7)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.068, 0.203); glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(-2.0, -0.70, -1.7)
    	glTexCoord2f(0.20, 0.24);  glVertex3f(-2.0, -0.70, -2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(0.0, -1.0, -2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(0.0, -0.70, -2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(0.0, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(0.0,-1.0, -1.7)
    	#muroesquerda
    	glTexCoord2f(0.30, 0.38);   glVertex3f(-2.0, -1.0, -2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(-2.0, -0.70, -2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(-2.0, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(-2.0, -1.0, -1.7)
   	glEnd()
    	#murograndelateraldireita
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.068, 0.38); glVertex3f(2.0, -1.0, 0.0)
    	glTexCoord2f(0.068, 0.25); glVertex3f(2.0, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(2.0, -0.70, 1.7)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(2.0, -1.0, 1.7)
    	#murofundo
    	glTexCoord2f(0.068, 0.38); glVertex3f(1.7, -1.0, 0.0)
    	glTexCoord2f(0.068, 0.25); glVertex3f(1.7, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(1.7, -0.70, 1.7)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(1.7, -1.0,  1.7)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(1.7, -0.699, 0.0)
    	glTexCoord2f(0.20, 0.24); glVertex3f(1.7, -0.699, 2.0)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(2.0, -0.699, 2.0)
    	glTexCoord2f(0.068, 0.203);  glVertex3f(2.0, -0.699, 0.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(1.7, -1.0, 0.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(1.7, -0.70, 0.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(2.0, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(2.0,-1.0, 1.7)
   	glEnd()
    	#murograndelatrealdireita
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.068, 0.38); glVertex3f(2.0, -1.0, -1.7)
    	glTexCoord2f(0.068, 0.25); glVertex3f(2.0, -0.70, -1.7)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(2.0, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(2.0, -1.0, 0.0)
    	#murofundo
    	glTexCoord2f(0.068, 0.38); glVertex3f(1.7, -1.0, -1.7)
    	glTexCoord2f(0.068, 0.25); glVertex3f(1.7, -0.70, -1.7)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(1.7, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(1.7, -1.0,  0.0)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(1.7, -0.699, -2.0)
    	glTexCoord2f(0.20, 0.24); glVertex3f(1.7, -0.699, 0.0)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(2.0, -0.699, 0.0)
    	glTexCoord2f(0.068, 0.203);  glVertex3f(2.0, -0.699, -2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(1.7, -1.0, -1.7)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(1.7, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(2.0, -0.70, 0.0)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(2.0,-1.0, 0.0)
    	glEnd()
    	#murograndelateralesquerda
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.068, 0.38); glVertex3f(-2.0, -1.0, 0.0)
    	glTexCoord2f(0.068, 0.25); glVertex3f(-2.0, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(-2.0, -0.70, 2.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(-2.0, -1.0, 2.0)
    	#murofundo
    	glTexCoord2f(0.068, 0.38); glVertex3f(-1.7, -1.0, 0.0)
    	glTexCoord2f(0.068, 0.25); glVertex3f(-1.7, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(-1.7, -0.70, 2.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(-1.7, -1.0,  2.0)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(-1.7, -0.699, 0.0)
    	glTexCoord2f(0.20, 0.24); glVertex3f(-1.7, -0.699, 2.0)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(-2.0, -0.699, 2.0)
    	glTexCoord2f(0.068, 0.203);  glVertex3f(-2.0, -0.699, 0.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(-1.7, -1.0, 0.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(-1.7, -0.70, 0.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(-2.0, -0.70, 1.7)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(-2.0,-1.0, 1.7)
    	#muroesquerda
    	glTexCoord2f(0.30, 0.38);   glVertex3f(-1.7, -1.0, 2.0)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(-1.7, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(-2.0, -0.70, 2.0)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(-2.0, -1.0, 2.0)
    	glEnd()
    	#murograndelatrealesquerda
    	glBegin(GL_QUADS)
    	#murofrente
    	glTexCoord2f(0.068, 0.38); glVertex3f(-2.0, -1.0, -1.7)
    	glTexCoord2f(0.068, 0.25); glVertex3f(-2.0, -0.70, -1.7)
    	glTexCoord2f(0.29, 0.25);  glVertex3f(-2.0, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(-2.0, -1.0, 0.0)
    	#murofundo
    	glTexCoord2f(0.068, 0.38); glVertex3f(-1.7, -1.0, -1.7)
    	glTexCoord2f(0.068, 0.25); glVertex3f(-1.7, -0.70, -1.7)
  	glTexCoord2f(0.29, 0.25);  glVertex3f(-1.7, -0.70, 0.0)
    	glTexCoord2f(0.29, 0.38);  glVertex3f(-1.7, -1.0,  0.0)
    	#murocima
    	glTexCoord2f(0.068, 0.24); glVertex3f(-1.7, -0.699, -2.0)
    	glTexCoord2f(0.20, 0.24); glVertex3f(-1.7, -0.699, 0.0)
    	glTexCoord2f(0.20, 0.203);  glVertex3f(-2.0, -0.699, 0.0)
    	glTexCoord2f(0.068, 0.203);  glVertex3f(-2.0, -0.699, -2.0)
    	#murodireita
    	glTexCoord2f(0.30, 0.38);   glVertex3f(-1.7, -1.0, -1.7)
    	glTexCoord2f(0.30, 0.25);   glVertex3f(-1.7, -0.70, -1.7)
    	glTexCoord2f(0.33, 0.25);  glVertex3f(-2.0, -0.70, 0.0)
    	glTexCoord2f(0.33, 0.38);  glVertex3f(-2.0,-1.0, 0.0)
    	glEnd()
    	#entrada
    	glBegin(GL_QUADS)
    	#entradafrente
    	glTexCoord2f(0.62, 0.52); glVertex3f(0.75, -1.0, 1.4)
    	glTexCoord2f(0.62, 0.48); glVertex3f(0.75, -0.95, 1.4)
    	glTexCoord2f(0.748, 0.48);  glVertex3f(1.37, -0.95, 1.4)
    	glTexCoord2f(0.748, 0.52);  glVertex3f(1.37, -1.0, 1.4)
    	#entradafundo
    	glTexCoord2f(0.62, 0.52); glVertex3f(0.75, -1.0, 1.201)
    	glTexCoord2f(0.62, 0.48); glVertex3f(0.75, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.48);  glVertex3f(1.37, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.52);  glVertex3f(1.37, -1.0, 1.201)
    	#entradacima
    	glTexCoord2f(0.62, 0.52); glVertex3f(0.75, -0.95, 1.4)
    	glTexCoord2f(0.62, 0.48);  glVertex3f(0.75, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.48);  glVertex3f(1.37, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.52);  glVertex3f(1.37, -0.95, 1.4)
    	#entradadireita
    	glTexCoord2f(0.62, 0.52);  glVertex3f(0.75, -1.0, 1.4)
    	glTexCoord2f(0.62, 0.48);  glVertex3f(0.75, -0.95, 1.4)
    	glTexCoord2f(0.748, 0.48);   glVertex3f(0.75, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.52);   glVertex3f(0.75, -1.0, 1.201)
    	#entradaesquerda
    	glTexCoord2f(0.62, 0.52); glVertex3f(1.37, -1.0, 1.4)
    	glTexCoord2f(0.62, 0.48);   glVertex3f(1.37, -0.95, 1.4)
    	glTexCoord2f(0.748, 0.48);  glVertex3f(1.37, -0.95, 1.201)
    	glTexCoord2f(0.748, 0.52);  glVertex3f(1.37, -1.0, 1.201)
	glTexCoord2f(0.90, 0.20);  glVertex3f(0.095, 1.1, -0.85)
    	glEnd()
        glDisable(GL_TEXTURE_2D)
	glEndList()

def InitGL(Width, Height):
    LoadTextures()
    CriarCasa()
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

xPassos = -19
zOlho = 4
xOlho = 20
yOlho = 0.2
zPassos = 4
yVoar = 0.2
def display():
    global xrot, yrot, zrot
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glCallList(id_casa)
    glPushMatrix()
    glTranslate(-8,0,0)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(-16,0,0)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(8,0,0)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(16,0,0)
    glCallList(id_casa)
    glPopMatrix()

    glPushMatrix()
    glRotate(180,0,1,0)
    glPushMatrix()
    glTranslate(0,0,-8)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(-8,0,-8)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(-16,0,-8)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(8,0,-8)
    glCallList(id_casa)
    glPopMatrix()
    glPushMatrix()
    glTranslate(16,0,-8)
    glCallList(id_casa)
    glPopMatrix()

    glPopMatrix()

    if id_mundo == -1:
        CriarMundo()
    else:
        glCallList(id_mundo)

    glDisable(GL_TEXTURE_2D)
    glTranslate(15,5,7)
    glColor3f(1,1,0)
    glutSolidSphere(0.8,70,70)
    glEnable(GL_TEXTURE_2D)
    glLoadIdentity()
    gluLookAt(xPassos,yVoar,zPassos,xOlho,yOlho,zOlho,0,1,0)
    glutSwapBuffers()

def teclaEspecialPressionada(tecla, x, y):
    global xPassos, zPassos, zOlho
    if tecla == GLUT_KEY_LEFT:
        if zPassos <=-5.5 or (xPassos>=-18.9 and xPassos <=-13.1 and zPassos <=3 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-10.9 and xPassos <=-5.1 and zPassos <=3 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=2.9 and zPassos <=3 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=10.9 and zPassos <=3 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=18.9 and zPassos <=3 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-18.9 and xPassos <=-13.1 and zPassos <=11 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-10.9 and xPassos <=-5.1 and zPassos <=11 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=2.9 and zPassos <=11 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=10.9 and zPassos <=11 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=18.9 and zPassos <=11 and zPassos>=5.6 and  yVoar <=2):
            zPassos -=0.0
        else:
            zPassos -=0.1
    elif tecla == GLUT_KEY_RIGHT:
        if zPassos >=13.5 or (xPassos>=-18.9 and xPassos <=-13.1 and zPassos <=2.99 and zPassos>=-3 and  yVoar <=2) or (xPassos>=-10.9 and xPassos <=-5.1 and zPassos <=2.99 and zPassos>=-3 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=2.9 and zPassos <=2.99 and zPassos>=-3 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=10.9 and zPassos <=2.99 and zPassos>=-3 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=18.9 and zPassos <=2.99 and zPassos>=-3 and  yVoar <=2) or (xPassos>=-18.9 and xPassos <=-13.1 and zPassos <=10.9 and zPassos>=5.5 and  yVoar <=2) or (xPassos>=-10.1 and xPassos <=-5.1 and zPassos <=10.9 and zPassos>=5.5 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=2.9 and zPassos <=10.9 and zPassos>=5.5 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=10.9 and zPassos <=10.9 and zPassos>=5.5 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=18.9 and zPassos <=10.9 and zPassos>=5.5 and  yVoar <=2):
            zPassos +=0.0
        else:
            zPassos +=0.1
    elif tecla == GLUT_KEY_UP:
	if  xPassos>=19.5 or (xPassos>=-19 and xPassos <=-13.1 and zPassos <=2.99 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-11 and xPassos <=-5.1 and zPassos <=2.99 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-3 and xPassos <=2.9 and zPassos <=2.99 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=5 and xPassos <=10.9 and zPassos <=2.99 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=13 and xPassos <=18.9 and zPassos <=2.99 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-19 and xPassos <=-13.1 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-11 and xPassos <=-5.1 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-3 and xPassos <=2.9 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=5 and xPassos <=10.9 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=13 and xPassos <=18.9 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2):
            xPassos += 0.0
	else:
        	xPassos += 0.1
    elif tecla == GLUT_KEY_DOWN:
	if xPassos<=-19.5 or (xPassos>=-18.9 and xPassos <=-13 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-10.9 and xPassos <=-5 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=3 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=11 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=19 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2) or (xPassos>=-18.9 and xPassos <=-13 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-10.9 and xPassos <=-5 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=-2.9 and xPassos <=3 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=5.1 and xPassos <=11 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2) or (xPassos>=13.1 and xPassos <=19 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2):
            xPassos -=0.0
	else:
            xPassos -= 0.1

def keyPressed(tecla, x, y):
    global yOlho, zOlho, yVoar
    if tecla == 'w' or tecla == 'W':
        yOlho +=0.2
    elif tecla == 's' or tecla == 'S':
        yOlho -=0.2
    elif tecla == 'd' or tecla == 'D':
        zOlho +=1
    elif tecla == 'a' or tecla == 'A':
        zOlho -=1
    elif tecla == 'f' or tecla == 'F':
        if yVoar >= 6.0:
            yVoar +=0
        else:
            yVoar +=0.1
    elif tecla == 'l' or tecla == 'L':
        if yVoar <= 0.2 or (xPassos>=-18.9 and xPassos <=-13 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2.1) or (xPassos>=-10.9 and xPassos <=-5 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2.1) or (xPassos>=-2.9 and xPassos <=3 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2.1) or (xPassos>=5.1 and xPassos <=11 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2.1) or (xPassos>=13.1 and xPassos <=19 and zPassos <=2.9 and zPassos>=-2.9 and  yVoar <=2.1) or (xPassos>=-18.9 and xPassos <=-13 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2.1) or (xPassos>=-10.9 and xPassos <=-5 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2.1) or (xPassos>=-2.9 and xPassos <=3 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2.1) or (xPassos>=5.1 and xPassos <=11 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2.1) or (xPassos>=13.1 and xPassos <=19 and zPassos <=10.9 and zPassos>=5.6 and  yVoar <=2.1):
            yVoar -=0
        else:
            yVoar -=0.1

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Casa")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(ReSizeGLScene)
    glutSpecialFunc(teclaEspecialPressionada)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()
if __name__ == "__main__":
    print "     *****    COMANDOS    *****\n"
    print " SETA PARA CIMA: ANDAR PARA FRENTE"
    print " SETA PARA BAIXO: ANDAR PARA TRAS"
    print " SETA PARA DIREITA: ANDAR PARA DIREITA"
    print " SETA PARA ESQUERDA: ANDAR PARA ESQUERDA"
    print " A: OLHAR PARA DIREITA"
    print " D: OLHAR PARA ESQUERDA"
    print " W: OLHAR PARA CIMA"
    print " S: OLHAR PARA BAIXO"
    print " F: VOAR"
    print " L: ATERRISAR"

    main()
