"""
Este progrma contiene weas
"""
import numpy as np
from math import cos,sin,radians #o usar lo que ya trae numpy

#______________Definir las funciones
def rotRx(xc,yc,zc,xp,yp,zp,Rx):
    a=[xp,yp,zp]
    b=[1,0,0] #--------Rx11,Rx12,Rx,13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx11+yp*Rx12+z
    b=[0,cos(Rx),-sin(Rx)]#---------Rx21,Rx22,Rx23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rz21+yp*Rx22+zp*Rx23
    b=[0,sin(Rx),cos(Rx)]#---------Rx31,Rx32,Rx33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz31+yp*Rx32+zp*Rx33
    [xg,yg,zg] = [xpp+xc,ypp+yc,zpp+zc]
    return [xg,yg,zg]

def rotRy(xc,yc,zc,xp,yp,zp,Ry):
    a=[xp,yp,zp]
    b=[cos(Ry),0,sin(Ry)] #--------Rx11,Rx12,Rx,13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx11+yp*Rx12+z
    b=[0,1,0]#---------Rx21,Rx22,Rx23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rz21+yp*Rx22+zp*Rx23
    b=[-sin(Ry),0,cos(Ry)]#---------Rx31,Rx32,Rx33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz31+yp*Rx32+zp*Rx33
    [xg,yg,zg] = [xpp+xc,ypp+yc,zpp+zc]
    return [xg,yg,zg]

def rotRz(xc,yc,zc,xp,yp,zp,Rz):

    a=[xp,yp,zp]
    b=[cos(Rz),-sin(Rz),0] #--------Rx11,Rx12,Rx,13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx11+yp*Rx12+z
    b=[sin(Rz),cos(Rz),0]#---------Rx21,Rx22,Rx23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rz21+yp*Rx22+zp*Rx23
    b=[0,0,1]#---------Rx31,Rx32,Rx33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz31+yp*Rx32+zp*Rx33
    [xg,yg,zg] = [xpp+xc,ypp+yc,zpp+zc]
    return [xg,yg,zg]

def fillStartCirckeValues(x,y,z,xg,yg,zg,phi1,phi2,dphi,r):
    for phi in np.arange(phi1,phi2+dphi,dphi): #Establecer las coordenadas de los puntos del circulo
        xp=r*cos(phi)
        yp=r*sin(phi)
        zp=0
        x.append(xp)
        y.append(yp)
        z.append(zp)
        xg.append(xp)
        yg.append(yp)
        zg.append(zp)
    return [x,y,z,xg,yg,zg]