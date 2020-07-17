#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-15)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   Assignment II 
#   upgrade form Assignment I
#----------------------------------------------------------------------



'''
credit
    for pygame https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos
    for delete circle https://stackoverflow.com/questions/1634509/is-there-any-way-to-clear-a-surface
    for mouse action https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect/21609309
    for non-overlap https://stackoverflow.com/questions/46702987/python-pygame-randomly-draw-non-overlapping-circles
    for boucing ball http://www.geometrian.com/programming/projects/index.php?project=Circle%20Collisions
'''



import pygame , random , math
#--------------------------------------
circle = 0
n = 6 #Max of number circle
i = 0 
FPS = 240
count = 0 #count of number circle
Cir = []
#----------------------------------------
pygame.init()

pygame.mouse.set_visible(1)
screen_w, screen_h = 800, 600
screen = pygame.display.set_mode( (screen_w, screen_h) )

pygame.display.set_caption('Assignment II')

clock = pygame.time.Clock()

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#----------------------------------------
#Class------------------------------------
class circle():
    def __init__(self):
        self.r = random.randint(10,20)
        self.x = random.randint(20,screen_w-self.r)
        self.y = random.randint(20,screen_h-self.r)
        self.R = random.randint(0,255)   
        self.G = random.randint(0,255)
        self.B = random.randint(0,255)
        self.color = (self.R,self.G,self.B,255)
        self.Speedx =0.3*(random.random()+1.0)
        self.Speedy =0.3*(random.random()+1.0)
#----------------------------------------

#funtion---------------------------------
def Biggest(target, All):
    ball_count = 0
    for F in All:
        if target != F:
            if target.r > F.r: ball_count+=1
            elif target.r == F.r: ball_count+=1
    if ball_count == len(All) - 1: return True
    else: return False
def delete():
    if event.type == pygame.MOUSEBUTTONDOWN:
        Mousex,Mousey = pygame.mouse.get_pos()
        A=0
        for C in Cir:
            cirx =(Mousex-Cir[A].x)**2
            ciry =(Mousey-Cir[A].y)**2
            if math.sqrt(cirx+ciry) <= Cir[A].r:
                if Biggest(C,Cir):
                    pygame.draw.circle(screen,(0,0,0,255), (int(Cir[A].x),int(Cir[A].y)), (Cir[A].r))
                    Cir.remove(C)
                    pygame.display.update()
            A+=1
def Draw_circle():
    screen.fill((0,0,0))
    for C in Cir:
        pygame.draw.circle(screen,C.color,(int(C.x),int(screen_h-C.y)),C.r)
    pygame.display.flip()

def CircleCollide(C1,C2):
    C1Speed = math.sqrt((C1.Speedx**2)+(C1.Speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.Speedx = XSpeed
    C1.Speedy = YSpeed

#LOOP------------------------------------
for a in range(n):
    Cir.append(circle())
#Running---------------------------------
running = True  
while running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #delete-------------------------------
    delete()
    #-------------------------------------

    #move---------------------------------
    for C in Cir:
        C.x += C.Speedx
        C.y += C.Speedy
    #create-------------------------------
    Draw_circle()
    #-------------------------------------

    #bounce/Collide-------------------------------

    for C in Cir:
        if C.x < C.r or C.x > screen_w-C.r: C.Speedx *= -1
        if C.y < C.r or C.y > screen_h-C.r: C.Speedy *= -1
    for C in Cir:
        for C_C in Cir:
            if C != C_C:
                if math.sqrt(  ((C.x-C_C.x)**2)  +  ((C.y-C_C.y)**2)  ) <= (C.r+C_C.r):
                    CircleCollide(C,C_C)
                    pygame.display.update()
#----------------------------------------------

#----------------------------------------------                
        

    screen.blit(surface,(0,0))
    pygame.display.update()
pygame.quit()