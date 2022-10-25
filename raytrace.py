# Les sources du Viok
# Raytrace 2022(c)CHEB from Amstrad 6128 old source 1987

import math
import sys
import msvcrt as m

import pygame
from pygame.locals import *

def main():
    # var ecrans
    width = 1280    
    height = 720

    # set le screen
    screen=pygame.display.set_mode((width,height))

    # pas en x et Y
    xm = 1
    ym = 1

    # Couleur
    # DATA 1,2,5,11,14,20,23,26,3,6,15,25
    # FOR n%=1 TO 12:READ c%:INK n%,c%:NEXT n%
    line_color = ["#101010", "#c1f0fe", "#90e4ff","#5fd9ff","#2ecdff", "#00c1fc","#00c1fc","#009bcc","#00769b", "#303030", "#202020", "#FFFFFF"]
    #             ombre dalle n           ciel1      c2                   c4                  c6                ombre dalle n         dalle blanc
    #                              c0                          c3                  c5                  c7                dalle noir
    # ? couleur rebond
    cl = [0,0,9,10,11,12]

    # 4 spheres
    nbs = 4

    # c : position sphere
    c = [[0,0,0,0],[0, -0.8,-1,3.2],[0,0,-0.45,2],[0,1.2,-0.7,2.5],[0,0.4,-1,4,0.4]]
    # r : rayon des spheres
    r = [0,0.7,0.3,0.5,0.4]
    # q : precalcul r²
    q = [0,0.7*0.7,0.3*0.3,0.5*0.5,0.4*0.4]
    # rc : retour col
    rc = 0
    dd = 0 
    s=0

    for i in range(0,height,ym):
        for j in range(0,width,xm):
            x = 0.3
            y = -0.5
            z = 0
            ba = 3
            dx = j-(width/2)
            dy = (height/2)-i
            dz = 1200
            dd = dx*dx + dy*dy + dz*dz
            # start ray
            while 1 == 1:
                # tant que le ray est en zone visible
                n = (y >= 0) or (dy <= 0)
                if not n:
                    #sol
                    s = -y/dy
                    n = 0
                else:
                    #ciel
                    n = -1
                
                # traitement des spheres
                for k in range(1,nbs+1):
                    px = c[k][1]-x
                    py = c[k][2]-y
                    pz = c[k][3]-z

                    pp = px*px + py*py + pz*pz
                    sc = px*dx + py*dy + pz*dz

                    if (sc > 0):
                        bb = (sc*sc)/ dd
                        aa = q[k] - pp + bb
                        if (aa > 0):
                            # ray dans sphere
                            sc = (math.sqrt(bb)-math.sqrt(aa))/math.sqrt(dd)
                            if (sc < s) or (n < 0):
                                # rebond
                                n = k
                                s = sc

                if (n < 0):
                    # Ciel
                    rc = 1 + int(((dy*dy)/dd)*15)
                    rc = setcol(i,j,xm,ym,rc)
                    pygame.draw.line(screen, line_color[rc], (j,height-i),(j+xm,height-i))
                    n = 0
                    # sortie du loop ray
                    break
                
                # Propagation preca
                dx = dx*s
                dy = dy*s
                dz = dz*s
                dd = dd*s*s
                
                x = x+dx
                y = y+dy
                z = z+dz
                
                if (n==0):
                    # Sol
                    for k in range(1,nbs+1):
                        u = c[k][1]-x
                        v = c[k][3]-z
                        if (u*u+v*v) <= q[k]:
                            ba=1
                    
                    if ((x % 1) > 0.5) == ((z % 1) > 0.5):
                        rc = cl[ba]
                    else:
                        rc = cl[ba+1]      

                    pygame.draw.line(screen, line_color[rc], (j,height-i),(j+xm,height-i))
                    # sortie du loop ray
                    break

                # Propagation suite
                nx = x-c[n][1]
                ny = y-c[n][2]
                nz = z-c[n][3]

                nn = nx*nx + ny*ny + nz*nz
                l = 2 * (dx*nx + dy*ny + dz*nz) / nn

                dx = dx - nx*l
                dy = dy - ny*l
                dz = dz - nz*l
                # rebond du rayon
            #Next pts
        # Affichage
        pygame.display.flip()
    m.getch()

# Calc couleur
def setcol(i,j,xm,ym,rc):
    l = ((j/xm)+(i/ym)) % 2
    if rc==2 and l==0:
        rc = 1
    elif rc==2 and l==1:
        rc = 2
    elif rc==3:
        rc = 2
    elif rc==4 and l==0:
        rc = 2
    elif rc==4 and l==1:
        rc = 3
    elif rc==5:
        rc = 3
    elif rc==6 and l==0:
        rc = 3
    elif rc==6 and l==1:
        rc = 4
    elif rc==7:
        rc = 4
    elif rc==8 and l==0:
        rc = 4
    elif rc==8 and l==1:
        rc = 5
    elif rc==9:
        rc = 5
    elif rc==10 and l==0:
        rc = 5
    elif rc==10 and l==1:
        rc = 6
    elif rc==11:
        rc = 6
    elif rc==12 and l==0:
        rc = 6
    elif rc==12 and l==1:
        rc = 7
    elif rc==13:
        rc = 7
    elif rc==14 and l==0:
        rc = 7
    elif rc==14 and l==1:
        rc = 8
    elif rc==15:
        rc = 8
    return rc 

# true code    
main()

