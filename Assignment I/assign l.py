#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-15)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   Assignment I
#
#----------------------------------------------------------------------



'''
credit
    for pygame https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos
    for delete circle https://stackoverflow.com/questions/1634509/is-there-any-way-to-clear-a-surface
    for mouse action https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect/21609309
    for non-overlap https://stackoverflow.com/questions/46702987/python-pygame-randomly-draw-non-overlapping-circles

'''



import pygame , random , math
circle = 0
n = 10 #Max of number circle
i = 0 
count = 0 #count of number circle
cir = []
pygame.init()


print( 'PyGame version: {}'.format( pygame.version.ver ) ) 

pygame.mouse.set_visible(1)
screen_w, screen_h = 800, 600
screen = pygame.display.set_mode( (screen_w, screen_h) )


pygame.display.set_caption('Assignment I')

clock = pygame.time.Clock()

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )


class circle():
    def __init__(self):
        self.r = random.choice([10,20])
        self.x = random.randint(20,screen_w-self.r)
        self.y = random.randint(20,screen_h-self.r)
        self.R = random.randint(0,255)   
        self.G = random.randint(0,255)
        self.B = random.randint(0,255)
        self.color = (self.R,self.G,self.B,255)
    def create_circle(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.r)
def Biggest(tar, All):
    ball_count = 0
    for F in All:
        if tar != F:
            if tar.r > F.r: ball_count+=1
            elif tar.r == F.r: ball_count+=1
    if ball_count == len(All) - 1: return True
    else: return False

running = True  
while running:
    clock.tick(10) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #create
    
    if count != n:
        cir.append('circle'+str(i))
        cir[i] = circle()
        Print = True
        for j in range(len(cir)):
            if i != j:
                distance = int(math.hypot(cir[i].x - cir[j].x, cir[i].y - cir[j].y))
                if distance < int(cir[i].r+cir[j].r):
                    Print = False
        if Print:
            count +=1
            cir[i].create_circle()
    i += 1
    #delete
    if event.type == pygame.MOUSEBUTTONDOWN:
        Mousex,Mousey = pygame.mouse.get_pos()
        a = 0
        for b in cir:
            cirx =(Mousex - cir[a].x)**2
            ciry =(Mousey - cir[a].y)**2
            if math.sqrt(cirx+ciry) <= cir[a].r:
                if Biggest(b,cir):
                    pygame.draw.circle(screen,(0,0,0,255), (cir[a].x,cir[a].y), (cir[a].r))
                    cir.remove(b)
            a+=1

    screen.blit(surface,(0,0))
    pygame.display.update()
pygame.quit()