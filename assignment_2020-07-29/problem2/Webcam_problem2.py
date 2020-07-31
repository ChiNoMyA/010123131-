#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-29)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   2020-07-29-WEBCAM_problem2
#
#----------------------------------------------------------------------
import pygame
import pygame.camera
from pygame.locals import *
import sys
#----------------------------------------------------------------------

#----------------------------------------
scr_w, scr_h = 1280, 720
col = 6 #row
row = 6 #collumn
rw, rh = scr_w//col, scr_h//row
img_rect,img_set = [],[]
#----------------------------------------

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    camera = None
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

def Switch_Pos(click_pos,rel_pos):
    #set click collumn and row
    click_pos_col,click_pos_row = click_pos[0]//(rw),click_pos[1]//(rh)
    #set click collumn and row
    rel_pos_col,rel_pos_row = rel_pos[0]//(rw),rel_pos[1]//(rh)
    #switch_Position
    img_rect[click_pos_col][click_pos_row],img_rect[rel_pos_col][rel_pos_row]=img_rect[rel_pos_col][rel_pos_row],img_rect[click_pos_col][click_pos_row]

pygame.init()

camera = open_camera()

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#set image list of list
for i in range(col):
    img_set = []
    for j in range(row):
        rect = (i*rw, j*rh, rw, rh)
        img_set.append(rect)
    img_rect.append(img_set)

img = None

is_running = True 
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
        #Mouse_click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
        #Mouse_Relese
        elif event.type == pygame.MOUSEBUTTONUP:
            rel_pos = pygame.mouse.get_pos()#get mouse position 
            Switch_Pos(click_pos,rel_pos)

    img = camera.get_image()#Update camera

    #Update position camera
    for i in range(col):
        for j in range(row):
            pygame.draw.rect( img,(0,255,0),img_rect[i][j],1)
            screen.blit( img,(i*rw,j*rh),img_rect[i][j] )
    
    #Update display
    pygame.display.update()
#stop camera and quit pygame
camera.stop()
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