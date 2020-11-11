import pygame
from pygame.locals import *
import sys
import time
import socket
import pygame
from network import Network

class Player() :
    def __init__(self,x,y,w,h,rightwalk,leftwalk,ground) :
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.rect = (x,y,w,h)
        self.vel = 6
        self.jump = False
        self.jump_height = 8
        self.right = True
        self.left = False
        self.atk = False
        self.fell = False
        self.fristfell = True
        self.fell_pos = (0,0)
        self.map = 1
        self.rightwalk = rightwalk 
        self.leftwalk = leftwalk
        self.ground = ground

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.atk = True 
        else:
            self.atk = False

        if keys[pygame.K_LEFT]:
            self.pos_x -= self.vel
            self.right = False
            self.left = True
        elif keys[pygame.K_RIGHT]:
            self.pos_x += self.vel
            self.right = True
            self.left = False
        
        if not self.jump:
            if keys[pygame.K_UP]:
                self.jump = True
        else:
            if self.jump_height >= -8:
                neg = 1
                if self.jump_height < 0:
                    neg = -1
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

    def fellHole(self,fellstart,fellend):
        if self.fell or (self.pos_x in range(fellstart,fellend-64) and self.pos_y in range(600-64,700)):
            
            if self.pos_x <= fellstart :
                self.pos_x = fellstart
            if self.pos_x >= fellend-64:
                self.pos_x = fellend-64 
            self.checkstatus()
            self.pos_y += self.vel
            
            self.fell = True
            if self.fristfell:
                self.fell_pos = [fellstart,fellend]
                self.fristfell = False
            
        else:
            self.fell =  False
    
    def checkMap(self):
        if self.map == 1:

            if self.pos_x < 0:
                self.pos_x = 0
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 2 

            for i in range(0,800,100):
                screen.blit(self.ground[(i//100)%2],(i,600))

        elif self.map == 2:

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 1
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 3
            
            for i in range(0,300,100):
                screen.blit(self.ground[(i//100)%2],(i,600))
            for i in range(400,600,100):
                screen.blit(self.ground[(i//100)%2],(i,600))
            for i in range(700,800,100):
                screen.blit(self.ground[(i//100)%2],(i,600))
            if self.fell:
                self.fellHole(self.fell_pos[0],self.fell_pos[1])
            else: 
                self.fellHole(300,400)
            if self.fell:
                self.fellHole(self.fell_pos[0],self.fell_pos[1])
            else:
                self.fellHole(600,700)

        elif self.map == 3:
            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 2
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 4
            for i in range(0,800,100):
                screen.blit(self.ground[(i//100)%2],(i,600))

def drawWindow(bg,player1,player2):
        screen.blit(bg,(0,-100))
        player1.checkMap()
        player2.checkMap()
        player1.checkstatus()
        player2.checkstatus()
        pygame.display.update()

def read_pos(str):
    str = str.split(",")
    return float(str[0]), float(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def read_status(list):
    return list


pygame.init()
pygame.display.set_caption('Shrimp Adventure') 
width = 800
height = 700
screen  = pygame.display.set_mode((width, height))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
clock = pygame.time.Clock()
bg = pygame.image.load('map1.png')
rightwalk = [pygame.image.load("Shrimp-front-atk.png"),pygame.image.load("Shrimp-front.png")]
leftwalk = [pygame.image.load("Shrimp-back-atk.png"),pygame.image.load("Shrimp-back.png")]
ground = [pygame.image.load('dirt-1.png'),pygame.image.load('dirt-2.png'),pygame.image.load('dirt-3.png')]
pic = [rightwalk,leftwalk,ground]

def main():
    net = Network()
    startPos = read_pos(net.getPos())

    player1 = Player(startPos[0],startPos[1],64,64,rightwalk,leftwalk,ground)
    player2 = Player(0,600-64,64,64,rightwalk,leftwalk,ground)
    run = True
    while run:
        clock.tick(60)
        playerPos = read_pos(net.send(make_pos((player1.pos_x, player1.pos_y))))
        
        player2.pos_x = playerPos[0]
        player2.pos_y = playerPos[1]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        drawWindow(bg,player1,player2) 

                  
main()
network.py



class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.189"
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