import pygame
from pygame.locals import *
import sys
import time
import socket
import pygame
#from network import Network

class Firer():
    def __init__(self,x,y,s) :
        self.pos_fire_x = x
        self.pos_fire_y = y
        self.side = s
        self.vel = 5*s
        self.attack = [pygame.image.load("fire.png"),pygame.image.load("fire-back.png")]
        self.monster_seal_atk = [pygame.image.load("seal-back-atk.png"),pygame.image.load("seal-front-atk.png")]
    def fire(self):
        if self.side == 1:
            screen.blit((self.attack[0]),(self.pos_fire_x+15,self.pos_fire_y))
        elif self.side == -1:
            screen.blit((self.attack[1]),(self.pos_fire_x-15,self.pos_fire_y))
    def monsterfire(self):
        if self.side == 1:
            screen.blit((self.monster_seal_atk[0]),(self.pos_fire_x+15,self.pos_fire_y))
        elif self.side == -1:
            screen.blit((self.monster_seal_atk[1]),(self.pos_fire_x-15,self.pos_fire_y))


class Monster():
    def __init__(self,x,y,m) :
        self.pos_x = x
        self.pos_y = y
        self.side = -1
        self.vel = 2 * self.side
        self.map = m
        self.rage = False
        self.hp = 3
        self.monster_fish =[pygame.image.load("fish-back.png"),pygame.image.load("fish-front.png")]
        self.monster_seal =[pygame.image.load("seal-back.png"),pygame.image.load("seal-front.png"),pygame.image.load("seal-back-rage.png"),pygame.image.load("seal-front-rage.png")]
    
    def deadMonster(self,fire_pos_x,fire_pos_y):
        if self.pos_x in range (fire_pos_x-32,fire_pos_x+32)  and self.pos_y in range(int(fire_pos_y)-16,int(fire_pos_y)+16) :
            if self.map == 2 or self.map == 4:
                self.hp -= 1
                if self.hp <= 0:
                    self.pos_y = -100
                return True
            elif self.map == 6 :
                self.hp -= 0.75
                if self.hp <= 0:
                    self.pos_y = -100
                return True
            elif self.map == 7 :
                self.hp -= 0.5
                if self.hp <= 0:
                    self.pos_y = -100
                return True
            else:
                self.hp -= 2
                if self.hp <= 0:
                    self.pos_y = -100
                return True

    def move(self):
        self.vel = 3 * self.side
        if self.map == 1:
            if self.side == 1:
                screen.blit((self.monster_fish[0]),(self.pos_x,self.pos_y))
            elif self.side == -1:
                screen.blit((self.monster_fish[1]),(self.pos_x,self.pos_y))
        if self.map == 2:
           if self.side == 1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[2]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[0]),(self.pos_x,self.pos_y))

           elif self.side == -1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[3]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[1]),(self.pos_x,self.pos_y))
        if self.map == 3:
            if self.side == 1:
                screen.blit((self.monster_fish[0]),(self.pos_x,self.pos_y))
            elif self.side == -1:
                screen.blit((self.monster_fish[1]),(self.pos_x,self.pos_y))
        if self.map == 4:
           if self.side == 1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[2]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[0]),(self.pos_x,self.pos_y))
           elif self.side == -1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[3]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[1]),(self.pos_x,self.pos_y))
        if self.map == 5:
            if self.side == 1:
                screen.blit((self.monster_fish[0]),(self.pos_x,self.pos_y))
            elif self.side == -1:
                screen.blit((self.monster_fish[1]),(self.pos_x,self.pos_y))
        if self.map == 6:
            if self.side == 1:
                screen.blit((self.monster_fish[0]),(self.pos_x,self.pos_y))
            elif self.side == -1:
                screen.blit((self.monster_fish[1]),(self.pos_x,self.pos_y))
        if self.map == 7 :
            if self.side == 1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[2]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[0]),(self.pos_x,self.pos_y))
            elif self.side == -1:
                if self.rage:
                    self.vel = 3 * self.side * 2
                    screen.blit((self.monster_seal[3]),(self.pos_x,self.pos_y))
                else:
                    screen.blit((self.monster_seal[1]),(self.pos_x,self.pos_y))


class Player() :
    def __init__(self,x,y,w,h) :
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.gui = [[i,j,100,100] for j in range(0,700,100) for i in range(0,800,100)]
        self.ground_map = []
        self.current_map = []
        self.side = 1
        self.vel = 8
        self.jump = False
        self.jump_height = 8
        self.right = True
        self.left = False
        self.atk = False
        self.Fire = []
        self.monster = None
        self.monster2 = None
        self.monster3 = None
        self.monster4 = None
        self.monster5 = None
        self.monster6 = None
        self.monster7 = None
        self.fristmap = True
        self.fristmap2 = True
        self.fristmap3 = True
        self.fristmap4 = True
        self.fristmap5 = True
        self.fristmap6 = True
        self.fristmap7 = True
        self.fell = False
        self.fristfell = True
        self.fell_pos = (0,0)
        self.map = 1
        self.rightwalk = [pygame.image.load("Shrimp-front-atk.png"),pygame.image.load("Shrimp-front.png")]
        self.leftwalk = [pygame.image.load("Shrimp-back-atk.png"),pygame.image.load("Shrimp-back.png")]
        self.ground = [pygame.image.load('dirt-1.png'),pygame.image.load('dirt-2.png'),pygame.image.load('dirt-3.png')]

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.atk = True 
            if self.right:
                self.side = 1
            elif self.left:
                self.side = -1
            if len(self.Fire) < 1:
                self.Fire.append(Firer(self.pos_x,self.pos_y,self.side))
        else:
            self.atk = False

        for f in self.Fire:
            if f.pos_fire_x < 800 and f.pos_fire_x > 0:
                f.pos_fire_x += f.vel
                if self.monster is not None:
                    if self.monster.deadMonster(f.pos_fire_x,f.pos_fire_y):
                        f.pos_fire_x += f.vel*1000
                
            else:
                self.Fire.pop(self.Fire.index(f))

        if keys[pygame.K_LEFT]:
            if check_left(self.pos_x,self.pos_y,self.current_map) :
                edge_left =  error_block(self.pos_x,self.pos_y,self.gui,'left',self.vel )
                if edge_left < self.vel :
                    self.pos_x -= edge_left
                    self.right = False
                    self.left = True
                else :
                    self.pos_x -= self.vel
                    self.right = False
                    self.left = True
        elif keys[pygame.K_RIGHT]:
            if check_right(self.pos_x,self.pos_y,self.current_map) :
                edge_right =  error_block(self.pos_x,self.pos_y,self.gui,'right',self.vel )
                if edge_right < self.vel :
                    self.pos_x += edge_right
                    self.right = True
                    self.left = False
                else :
                    self.pos_x += self.vel
                    self.right = True
                    self.left = False

        index = check_ground(self.pos_x,self.pos_y,self.current_map)
        head_index = check_head(self.pos_x,self.pos_y,self.current_map)
        if not self.jump and self.pos_y +64 >= self.current_map[index][1] and index != -1 :
            if keys[pygame.K_UP]:
                self.jump = True
        elif self.jump :
            if self.jump_height >= -8:
                neg = 1
                if self.jump_height < 0 :
                    if self.pos_y +64 < self.current_map[index][1] :
                        neg = -1
                        if self.current_map[index][1] - (self.pos_y + 64) < (self.jump_height**2) * 0.6 :
                            self.pos_y -= (self.current_map[index][1] - (self.pos_y + 64)) * neg
                        else :
                            self.pos_y -= (self.jump_height**2) * 0.6 * neg
                        self.jump_height -= 1
                    elif self.pos_y +64 >= self.current_map[index][1] :
                        neg = 0
                        self.pos_y -= (self.jump_height**2) * 0.6 * neg
                        self.jump_height -= 1
                else :
                    vel = error_block(self.pos_x,self.pos_y,self.gui,'top',(self.jump_height**2) * 0.6 )
                    if  self.pos_y <= self.current_map[head_index][1] + self.current_map[head_index][3] and head_index != -1 :
                        self.jump_height = 0
                        self.pos_y -= (self.jump_height**2) * 0.6 * neg
                        self.jump_height -= 1
                    else :
                        if vel < (self.jump_height**2) * 0.6  :
                            self.pos_y -= vel * neg
                            self.jump_height -= 1
                        else :
                            self.pos_y -= (self.jump_height**2) * 0.6 * neg
                            self.jump_height -= 1
            else:
                self.jump = False
                self.jump_height = 8
    
    def checkstatus(self):
        if self.right:
            if self.atk:
                screen.blit((self.rightwalk[0]),(self.pos_x,self.pos_y))    
            else:
                screen.blit((self.rightwalk[1]),(self.pos_x,self.pos_y))
        elif self.left:
            if self.atk:
                screen.blit((self.leftwalk[0]),(self.pos_x,self.pos_y))
            else:
                screen.blit((self.leftwalk[1]),(self.pos_x,self.pos_y))
        for f in self.Fire:
            f.fire()
        
        
        

    def fellHole(self,ground):
        for i in ground :
            if (self.pos_x in range(i[0],i[0] + i[2]) or (self.pos_x + self.width) in range(i[0],i[0] + i[2])):
                if i[1] - (self.pos_y + 64) == 0 and i[1] - (self.pos_y) == 64:
                    self.fell =  False
                    break
            else :
                self.fell = True
    
    def checkMap(self):
        if self.map == 1:

            if self.fristmap:
                self.monster = Monster(500,600-64,self.map)
                self.fristmap = False
            
            if self.monster.pos_x > 800-64 :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x < 0:
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x >= 0 and self.monster.pos_x <= 800:
                self.monster.pos_x += self.monster.vel
            
            self.monster.move()
            '''
            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y):
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.monster.pos_x = 500
                print('dead not big surpise')
                '''
            if self.pos_x < 0:
                self.pos_x = 0
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 2
                self.fristmap = True
                self.monster = None
                self.Fire = []

            index = 0
            for i in range(0,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            self.current_map = self.ground_map

            

            self.ground_map = []

        elif self.map == 2:
            
            if self.fristmap:
                self.monster = Monster(500,600-64,self.map)
                self.fristmap = False

            if firemonster(self.monster.pos_x,self.monster.pos_y,self.monster.side,self.pos_x,self.pos_y):
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True


            if self.monster.pos_x > 800-64 :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x < 0:
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel
                self.monster.rage = True
            elif self.monster.pos_x >= 0 and self.monster.pos_x <= 800:
                self.monster.pos_x += self.monster.vel
            
            self.monster.move()

            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')
            if self.pos_y > 700 :
                dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y)
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 1
                self.fristmap = True
                self.monster = None
                self.Fire = []
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 3
                self.fristmap = True
                self.monster = None
                self.Fire = []
            
            
            index = 0
            for i in range(0,300,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            for i in range(400,600,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            for i in range(700,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1

            self.current_map = self.ground_map
            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    if (self.pos_x in range(self.current_map[index_g][0],self.current_map[index_g][0] + self.current_map[index_g][2]) or (self.pos_x + self.width) in range(self.current_map[index_g][0],self.current_map[index_g][0] + self.current_map[index_g][2])):
                        if self.current_map[index_g][1] == (self.pos_y + 64) :
                            self.fell = False
                        else :
                            self.checkstatus()
                            vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                            if self.vel > vel :
                                self.pos_y += vel
                            else :
                                self.pos_y += self.vel
                    else :
                            self.checkstatus()
                            vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                            if self.vel > vel :
                                self.pos_y += vel
                            else :
                                self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)

            self.ground_map = []

        elif self.map == 3:
            if self.fristmap:
                self.monster = Monster(500,600-64,self.map)
                self.fristmap = False
            
            if self.monster.pos_x > self.pos_x :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel*3
            elif self.monster.pos_x < self.pos_x :
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel*3

            self.monster.move()

            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 2
                self.fristmap = True
                self.monster = None
                self.Fire = []
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 4
                self.fristmap = True
                self.monster = None
                self.Fire = []
            index = 0
            for i in range(0,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1

            self.current_map = self.ground_map
            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    if (self.pos_x in range(self.current_map[index_g][0],self.current_map[index_g][0] + self.current_map[index_g][2]) or (self.pos_x + self.width) in range(self.current_map[index_g][0],self.current_map[index_g][0] + self.current_map[index_g][2])):
                        if self.current_map[index_g][1] == (self.pos_y + 64) :
                            self.fell = False
                        else :
                            #print(self.current_map[index_g][1],self.pos_y,index_g)
                            self.checkstatus()
                            vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                            if self.vel > vel :
                                self.pos_y += vel
                            else :
                                self.pos_y += self.vel
                    else :
                            #print(self.current_map[index_g][1],self.pos_y,index_g)
                            self.checkstatus()
                            vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                            if self.vel > vel :
                                self.pos_y += vel
                            else :
                                self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)

                    
            self.ground_map = []
        
        elif self.map == 4:
            
            if self.fristmap:
                self.monster = Monster(500,600-64,self.map)
                self.fristmap = False

            if self.monster.pos_x > 800-64 :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x < 300:
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel
                self.monster.rage = True
            elif self.monster.pos_x >= 300 and self.monster.pos_x <= 800:
                self.monster.pos_x += self.monster.vel

            self.monster.move()

            if firemonster(self.monster.pos_x,self.monster.pos_y,self.monster.side,self.pos_x,self.pos_y):
               self.pos_x = 0
               self.pos_y = 600 - 64
               self.map = 1
               self.fristmap = True
            
            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 3
                self.fristmap = True
                self.monster = None
                self.Fire = []
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 5
                self.fristmap = True
                self.monster = None
                self.Fire = []

            index = 0
            self.ground_map.append([0 , 600 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
            index += 1
            for i in range(100,300,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],600))
                index += 1
            for i in range(300,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            self.ground_map.append([100 , 500 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            self.ground_map.append([200 , 500 , 100 , 100])
            screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            self.ground_map.append([200 , 400 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1

            self.current_map = self.ground_map

            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    if self.current_map[index_g][1] == (self.pos_y + 64) or self.pos_x == 0 or self.pos_x == 800 :
                        self.fell = False
                    else :
                        self.checkstatus()
                        vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                        if self.vel > vel :
                            self.pos_y += vel
                        else :
                            self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)

            

            self.ground_map = []
        
        elif self.map == 5:
            
            if self.fristmap:
                self.monster = Monster(600,300-64,self.map)
                self.fristmap = False

            if self.monster.pos_x > 600-64 :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x < 300:
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel
                self.monster.rage = True
            elif self.monster.pos_x >= 300 and self.monster.pos_x <= 600:
                self.monster.pos_x += self.monster.vel
            
            self.monster.move()

            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 4
                self.fristmap = True
                self.monster = None
                self.Fire = []
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 6
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                self.monster2 = None
                self.monster3 = None
                self.monster4 = None
                self.monster5 = None
                self.monster6 = None
                self.monster7 = None
                self.Fire = []

            index = 0
            for i in range(100,300,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([200 , 500 , 100 , 100])
            screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(400,700,100):
                self.ground_map.append([500 , i , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([700 , 600 , 100 , 100])
            screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(200,400,100):
                self.ground_map.append([700 , i , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([300 , 600 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(600,800,100):
                self.ground_map.append([i , 1200 - i , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            for i in range(0,300,100):
                self.ground_map.append([i , 600 - i , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            for i in range(400,600,100):
                self.ground_map.append([i , 800 - i , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([700 , 100 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
    

            self.current_map = self.ground_map

            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    if self.current_map[index_g][1] == (self.pos_y + 64) or self.pos_x == 0 or self.pos_x == 800 :
                        self.fell = False
                    else :
                        self.checkstatus()
                        vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                        if self.vel > vel :
                            self.pos_y += vel
                        else :
                            self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)
            

            self.ground_map = []

        elif self.map == 6:

            if self.fristmap:
                self.monster = Monster(400,600-64,self.map)
                self.fristmap = False

            if self.monster.pos_x > 500-64 :
                self.monster.side = -1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x < 0:
                self.monster.side = 1
                self.monster.pos_x += self.monster.vel
            elif self.monster.pos_x >= 0 and self.monster.pos_x <= 500-64 :
                self.monster.pos_x += self.monster.vel
            
            self.monster.move()

            if dead(self.pos_x,self.pos_y,self.monster.pos_x,self.monster.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')



            if self.fristmap2:
                self.monster2 = Monster(500,100-64,self.map)
                self.fristmap2 = False

            if self.monster2.pos_x > 600-64 :
                self.monster2.side = -1
                self.monster2.pos_x += self.monster2.vel*2
            elif self.monster2.pos_x < 0:
                self.monster2.side = 1
                self.monster2.pos_x += self.monster2.vel*2
            elif self.monster2.pos_x >= 0 and self.monster2.pos_x <= 600-64 :
                self.monster2.pos_x += self.monster2.vel*2
            
            self.monster2.move()

            if dead(self.pos_x,self.pos_y,self.monster2.pos_x,self.monster2.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')


            if self.fristmap3:
                self.monster3 = Monster(618,400-64,self.map)
                self.fristmap3 = False

            if self.monster3.pos_y > 700-64 :
                self.monster3.side = -1
                self.monster3.pos_y += self.monster3.vel*3
            elif self.monster3.pos_y < 100:
                self.monster3.side = 1
                self.monster3.pos_y += self.monster3.vel*3
            elif self.monster3.pos_y >= 100 and self.monster3.pos_y <= 700-64 :
                self.monster3.pos_y += self.monster3.vel*3
            
            self.monster3.move()

            if dead(self.pos_x,self.pos_y,self.monster3.pos_x,self.monster3.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')


            if self.fristmap4:
                self.monster4 = Monster(418,300-64,self.map)
                self.fristmap4 = False

            if self.monster4.pos_y > 600-64 :
                self.monster4.side = -1
                self.monster4.pos_y += self.monster4.vel*2
            elif self.monster4.pos_y < 0:
                self.monster4.side = 1
                self.monster4.pos_y += self.monster4.vel*2
            elif self.monster4.pos_y >= 0 and self.monster4.pos_y <= 600-64 :
                self.monster4.pos_y += self.monster4.vel*2
            
            self.monster4.move()

            if dead(self.pos_x,self.pos_y,self.monster4.pos_x,self.monster4.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')


            if self.fristmap5:
                self.monster5 = Monster(118,300-64,self.map)
                self.fristmap5 = False

            if self.monster5.pos_y > 400-64 :
                self.monster5.side = -1
                self.monster5.pos_y += self.monster5.vel*2
            elif self.monster5.pos_y < 0:
                self.monster5.side = 1
                self.monster5.pos_y += self.monster5.vel*2
            elif self.monster5.pos_y >= 0 and self.monster5.pos_y <= 400-64 :
                self.monster5.pos_y += self.monster5.vel*2
            
            self.monster5.move()

            if dead(self.pos_x,self.pos_y,self.monster5.pos_x,self.monster5.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')


            if self.fristmap6:
                self.monster6 = Monster(218,400-64,7)
                self.fristmap6 = False

            if self.monster6.pos_x > 700-64 :
                self.monster6.rage = True
                self.monster6.side = -1
                self.monster6.pos_x += self.monster6.vel
            elif self.monster6.pos_x < 100:
                self.monster6.side = 1
                self.monster6.pos_x += self.monster6.vel
            elif self.monster6.pos_x >= 100 and self.monster6.pos_x <= 700-64 :
                self.monster6.pos_x += self.monster6.vel
            
            self.monster6.move()

            if dead(self.pos_x,self.pos_y,self.monster6.pos_x,self.monster6.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                print('dead not big surpise')


            if self.fristmap7:
                self.monster7 = Monster(700,200-64,7)
                self.fristmap7 = False

            if self.monster7.pos_x > 800-64 :
                self.monster7.side = -1
                self.monster7.pos_x += self.monster7.vel
            elif self.monster7.pos_x < 400:
                self.monster7.rage = True
                self.monster7.side = 1
                self.monster7.pos_x += self.monster7.vel
            elif self.monster7.pos_x >= 400 and self.monster6.pos_x <= 800-64 :
                self.monster7.pos_x += self.monster7.vel
            
            self.monster7.move()

            if firemonster(self.monster7.pos_x,self.monster7.pos_y,self.monster7.side,self.pos_x,self.pos_y):
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None

            if dead(self.pos_x,self.pos_y,self.monster7.pos_x,self.monster7.pos_y) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                self.fristmap2 = True
                self.fristmap3 = True
                self.fristmap4 = True
                self.fristmap5 = True
                self.fristmap6 = True
                self.fristmap7 = True
                self.monster = None
                self.monster2 = None
                self.monster3 = None
                self.monster4 = None
                self.monster5 = None
                self.monster6 = None
                self.monster7 = None
                print('dead not big surpise')

            if self.pos_x < 0 :
                if 400 < self.pos_y + 64 < 500 :
                    self.pos_x = 800
                    self.map = 5
                    self.fristmap = True
                    self.fristmap2 = True
                    self.fristmap3 = True
                    self.fristmap4 = True
                    self.fristmap5 = True
                    self.fristmap6 = True
                    self.fristmap7 = True
                    self.monster = None
                    self.monster2 = None
                    self.monster3 = None
                    self.monster4 = None
                    self.monster5 = None
                    self.monster6 = None
                    self.monster7 = None
                    self.Fire = []
                else :
                    self.pos_x = 0
            elif self.pos_x + 64 > 800:
                screen.fill((255,255,255))
                font = pygame.font.Font('freesansbold.ttf', 64) 
                text = font.render('YOU WIN',True,(0,0,0)) 
                textRect = text.get_rect() 
                textRect.center = (800 // 2, 700 // 2) 
                screen.blit(text, textRect) 
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()

            index = 0
            for i in range(0,500,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            for i in range(400,700,100):
                self.ground_map.append([700 , i , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([500 , 600 , 100 , 100])
            screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(100,400,100):
                self.ground_map.append([i , 400 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([700 , 300 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(200,400,100):
                self.ground_map.append([i , 400 - i , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([0 , 300 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            for i in range(600,800,100):
                self.ground_map.append([i , 0 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
                index += 1
            self.ground_map.append([500 , 500 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            self.ground_map.append([500 , 200 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
    

            self.current_map = self.ground_map

            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    #print(index_g,self.current_map[index_g][1],self.pos_y + 64)
                    if self.current_map[index_g][1] == (self.pos_y + 64) or self.pos_x == 0 or self.pos_x == 800 :
                        self.fell = False
                    else :
                        self.checkstatus()
                        vel = error_block(self.pos_x,self.pos_y,self.gui,'bottom',self.vel)
                        if self.vel > vel :
                            self.pos_y += vel
                        else :
                            self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)
            if dead(self.pos_x,self.pos_y,0,0) :
                self.pos_x = 0
                self.pos_y = 600 - 64
                self.map = 1
                self.fristmap = True
                print('dead not big surpise')

            self.ground_map = []

def drawWindow(bg,player1,player2):
        screen.blit(bg,(0,-100))
        player1.checkMap()
        player2.checkMap()
        player1.checkstatus()
        player2.checkstatus()
        pygame.display.update()

def read_pos(string):
    string = string.split(",")
    return float(string[0]), float(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def firemonster(x,y,s,px,py):
    if len(Monsterfire) < 1:
        Monsterfire.append(Firer(x,y,s))
    for f in Monsterfire:
        if f.pos_fire_x < 800 and f.pos_fire_x > 0:
            f.pos_fire_x += f.vel
            Dead = deadfire(f.pos_fire_x,f.pos_fire_y,px,py)
            if Dead:
                f.pos_fire_x +=f.vel * 1000
                return True
        else:
            Monsterfire.pop(Monsterfire.index(f))

    for f in Monsterfire:
        f.monsterfire()
def check_ground(x,y,data) :
    index = -1
    for i in range(len(data)) :
        if (data[i][0] < x < data[i][0] + data[i][2] or data[i][0] < x + 64 < data[i][0] + data[i][2])   :#or data[i][1].point_x < pos.point_x + 64 < data[i][1].point_x + data[i][1].wide):
            if (y +64 <= data[i][1] and y <= data[i][1] ) :
                index = i
    return index

def check_head(x,y,data) :
    index = -1
    for i in range(len(data)) :
        if (data[i][0] < x < data[i][0] + data[i][2] or data[i][0] < x + 64 < data[i][0] + data[i][2]) and y >= data[i][1] +  data[i][3] and y +64 >= data[i][1] +  data[i][3] and y - (data[i][1] +  data[i][3]) <= 36 :#or data[i][1].point_x < pos.point_x + 64 < data[i][1].point_x + data[i][1].wide):
            index = i
    return index

def check_left(x,y,data) :
    process = True
    for i in range(len(data)) :
        if x == data[i][0]+ data[i][2] :
            if (data[i][1] < y + 64 < data[i][1] + data[i][3] or data[i][1] < y < data[i][1] + data[i][3]):
                process = False
                break
            else:
                process = True
        else :
            pass
    return process

def check_right(x,y,data) :
    process = True
    for i in range(len(data)) :
        if x + 64 >= data[i][0] and x < data[i][0]:
            if (data[i][1] < y + 64 < data[i][1] + data[i][3] or data[i][1] < y < data[i][1] + data[i][3]):
                process = False
                break
            else:
                process = True
        else :
            pass
    return process

def error_block(x,y,data,direction,diff) :
    process = diff
    for i in range(len(data)) :
        if direction == 'left':
            if data[i][0] < x  < data[i][0] + data[i][2] :
                if (x - data[i][0]) < diff :
                    process = (x - data[i][0])
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'right':
            if data[i][0] < x +64  < data[i][0] + data[i][2] :
                if ((data[i][0] + data[i][2]) - (x + 64)) < diff :
                    process = ((data[i][0] + data[i][2]) - (x + 64))
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'top':
            if data[i][1] < y  < data[i][1] + data[i][3] :
                if (y - data[i][1]) < diff :
                    process = (y - data[i][1])
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'bottom':
            if data[i][1] < y + 64 < data[i][1] + data[i][3] :
                if ((data[i][1] + data[i][3]) - (y +64)) < diff :
                    process = ((data[i][1] + data[i][3]) - (y +64))
                    break
                else :
                    process = diff
                    break

            else :
                pass
    return process

def deadfire(fire_pos_x,fire_pos_y,pos_x,pos_y):
    if fire_pos_x in range(pos_x-32,pos_x+32)  and fire_pos_y == pos_y : 
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 64) 
        text = font.render('Game over',True,(0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (800 // 2, 700 // 2) 
        screen.blit(text, textRect) 
        pygame.display.update()
        pygame.time.delay(1000)
        return True
def dead(x,y,enemy_x,enemy_y) :
    dead = False 
    if x < enemy_x + 10 < x + 64 or x < enemy_x + 54 < x + 64 or y > 700:
        if y <= enemy_y + 10 <= y + 64 or y <= enemy_y + 54 <= y + 64 or y > 700:
            dead = True 
            screen.fill((255,255,255))
            font = pygame.font.Font('freesansbold.ttf', 64) 
            text = font.render('Game over',True,(0,0,0)) 
            textRect = text.get_rect() 
            textRect.center = (800 // 2, 700 // 2) 
            screen.blit(text, textRect) 
            pygame.display.update()
            pygame.time.delay(1000)
        else :
            dead = False
    else :
        dead = False

    return dead

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.110"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


pygame.init()
pygame.display.set_caption('Shrimp Adventure') 
width = 800
height = 700
screen  = pygame.display.set_mode((width, height))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
clock = pygame.time.Clock()
bg = pygame.image.load('map1.png')
Monsterfire=[]


def main():

    net = Network()
    startPos = read_pos(net.getPos())
    player1 = Player(0,600-64,64,64)
    player2 = Player(300,600-64,64,64)
    run = True
    while run:
        clock.tick(60)
        p2Pos = read_pos(net.send(make_pos((player1.pos_x, player1.pos_y))))
        player2.pos_x = p2Pos[0]
        player2.pos_y = p2Pos[1]


        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()
        drawWindow(bg,player1,player2) 
        player1.move()

                  
main()
network.py
