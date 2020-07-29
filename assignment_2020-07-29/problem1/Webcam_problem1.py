#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-29)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   2020-07-29-WEBCAM_problem1
#
#----------------------------------------------------------------------
import pygame
from pygame.locals import *
import sys

#I can't use camera,It Error is "vidcap.Error: Cannot set capture resolution."
#----------------------------------------------------------------------

#----------------------------------------
scr_w, scr_h = 640, 480
rol = 6 #roll
col = 6 #collumn
rw, rh = scr_w//rol, scr_h//col
Rect=[]
#----------------------------------------


pygame.init()

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#import image
img=pygame.image.load("C://Users//66912//Pictures//Camera Roll//pygame_cam.jpg")
surface.blit( img,(0,0))
class RECT():
    def __init__(self,i,j):
        self.x = i*rw
        self.y = j*rh
        self.rect = (i*rw, j*rh, rw, rh)
        self.color = (0,0,0,255)
'''
for i in range(rol):
    for j in range(col):
        rect = (i*rw, j*rh, rw, rh)
        Rect.append(RECT(i,j))
        screen.fill((0,0,0))
        pygame.draw.rect(surface ,(0,255,0), rect, 1)
'''
is_running = True 
while is_running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
    
    if e.type == pygame.MOUSEBUTTONDOWN:
        Mousex,Mousey = pygame.mouse.get_pos()
        A=0
        for R in Rect:
            recx = Rect[A].x + rw
            recy = Rect[A].y + rh
            if (Mousex >= Rect[A].x and Mousex <= recx) and (Mousey >= Rect[A].y and Mousey <= recy):
                rect_del = (Rect[A].x, Rect[A].y, rw, rh)
                surface.blit( img, rect_del, rect_del )
                Rect.remove(R)
            A+=1

    # write the surface to the screen and update the display
    screen.blit(surface, (0,0))
    pygame.display.update()

pygame.quit()
#----------------------------------------------------------------------


'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
---             ---   -----   ----        -----   -----   ---   ---   ---   ------   ----         ----   -----   ------         -----          ---          -------
--------   --------   -----   ---   -----   ---     ---   ---   --   -----   ----   ----    ---    ---   -----   ------   ----   ---   -----------   -----   ------
--------   --------   -----   ---   -----   ---      --   ---   -   -------   --   -----   -----   ---   -----   ------   ----   ---   -----------   -----   ------
--------   --------           ---   -----   ---   -   -   ---      ---------     -------   -----   ---   -----   ------         -----         ----          -------
--------   --------   -----   ---           ---   --      ---   --   --------   --------   -----   ---   -----   ------   ---   ------------   ---   --------------
--------   --------   -----   ---   -----   ---   ---     ---   ---   -------   --------    ---    ---   -----   ------   ----   -----------   ---   --------------
--------   --------   -----   ---   -----   ---   ----    ---   ----   ------   ---------         -----         -------   -----   ---         ----   --------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''