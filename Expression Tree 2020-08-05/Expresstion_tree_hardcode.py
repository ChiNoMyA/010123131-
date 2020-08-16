#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-24)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   2020-08-05 class for calculator
#   !!!!!!!!!!!!!!BUT IT HARD CODE!!!!!!!!!!!!!!
#----------------------------------------------------------------------

import pygame
import sys

List_tree = ['+',['&','I0','I1'],['!',['&','I1','I2']]]

scr_w,scr_h = 1000,600
H = len(List_tree)
row_pos = []
col_pos = []
row_h = int(scr_h/4)
col_w = int(scr_w/4)
for i in range(4):
    row_pos.append(int(row_h*(i+1)-100))
for i in range(4):
    col_pos.append(int(col_w*(i+1)))

pygame.init()

screen = pygame.display.set_mode((scr_w, scr_h))

font = pygame.font.Font(None, 100)
clock = pygame.time.Clock()

color_circle = pygame.Color('limegreen')
color_text = pygame.Color('lightyellow2')
running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, color_circle, (col_pos[1],row_pos[0]), (col_pos[0],row_pos[1]),25)
    pygame.draw.line(screen, color_circle, (col_pos[1],row_pos[0]), (col_pos[2],row_pos[1]),25)
    pygame.draw.line(screen, color_circle, (col_pos[0],row_pos[1]), (col_pos[0]-100,row_pos[2]),25)
    pygame.draw.line(screen, color_circle, (col_pos[0],row_pos[1]), (col_pos[0]+100,row_pos[2]),25)
    pygame.draw.line(screen, color_circle, (col_pos[2],row_pos[1]), (col_pos[2],row_pos[2]),25)
    pygame.draw.line(screen, color_circle, (col_pos[2],row_pos[2]), (col_pos[2]-100,row_pos[3]),25)
    pygame.draw.line(screen, color_circle, (col_pos[2],row_pos[2]), (col_pos[2]+100,row_pos[3]),25)

    text = '+'
    input_circle = (col_pos[1],row_pos[0])
    input_text = (col_pos[1]-20,row_pos[0]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = '&'
    input_circle = (col_pos[0],row_pos[1])
    input_text = (col_pos[0]-20,row_pos[1]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = 'I0'
    input_circle = (col_pos[0]-100,row_pos[2])
    input_text = (col_pos[0]-120,row_pos[2]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = 'I1'
    input_circle = (col_pos[0]+100,row_pos[2])
    input_text = (col_pos[0]+80,row_pos[2]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = '!'
    input_circle = (col_pos[2],row_pos[1])
    input_text = (col_pos[2]-20,row_pos[1]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = '&'
    input_circle = (col_pos[2],row_pos[2])
    input_text = (col_pos[2]-20,row_pos[2]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = 'I1'
    input_circle = (col_pos[2]-100,row_pos[3])
    input_text = (col_pos[2]-120,row_pos[3]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)

    text = 'I2'
    input_circle = (col_pos[2]+100,row_pos[3])
    input_text = (col_pos[2]+80,row_pos[3]-40)
    txt_surface = font.render(text, True, color_text)
    pygame.draw.circle(screen, color_circle, input_circle,50)
    screen.blit(txt_surface, input_text)
    
    

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

