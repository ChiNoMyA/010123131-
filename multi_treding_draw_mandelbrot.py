#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-07-24)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   2020-07-22-mandelbrot_threading
#
#----------------------------------------------------------------------

'''
credit
    for Mandelbrot --> python_threading_demo-8.py by RSP
    for Mandelbrot funtion --> https://en.wikipedia.org/wiki/Mandelbrot_set?fbclid=IwAR092TqXGASrq-ro3g5OgWHP4HxMroUD04ln86tSYX08Nw7OSlJNphJSP6Q
'''
#Import zone
#----------------------------------------------------------------------
import threading,time,cmath,pygame
from random import randint, randrange, random
#----------------------------------------------------------------------

#Global zone
#----------------------------------------------------------------------
FPS=240#clocktick
scr_w, scr_h = 500, 500#Screen
running = True #Running pygame
#----------------------------------------------------------------------

#Funtion zone
#----------------------------------------------------------------------
def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

def thread_func(id,surface,lock,barrier,):
    x_min=id * 5
    x_max=x_min+100
    y_min,y_max=0,500
    scale = 0.006
    offset = complex(-0.55,0.0)
    while x_min <= x_max:
        while y_min <= y_max :
            re = scale*(x_min-w2) + offset.real
            im = scale*(y_max-h2) + offset.imag
            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            with lock:
                surface.set_at( (x_min, y_max), (255-r,255-g,255-b) )
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                pass
            y_max-=1
        y_max=500
        x_min+=1
#----------------------------------------------------------------------


#Start Zone
#----------------------------------------------------------------------
pygame.init() # initialize pygame

screen = pygame.display.set_mode( (scr_w, scr_h) )  # create a screen of width=500 and height=500

pygame.display.set_caption('Fractal Image: Mandelbrot multi_treding') # set window caption

clock = pygame.time.Clock() # create a clock

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )  # create a surface for drawing

N = 100 # set the number of threads to be created

lock = threading.Lock() # create a thread lock 

barrier = threading.Barrier(N+1)    # create a barrier

list_threads = []   # a list for keeping the thread objects

w2, h2 = scr_w/2, scr_h/2   # half width, half screen
#----------------------------------------------------------------------

#Running Zone
#----------------------------------------------------------------------
for i in range(N):
    id = (i+1)
    t = threading.Thread(target=thread_func, args=(id,surface,lock,barrier))
    t.setName( 'Thread_mandlebrot-{:03d}'.format(id) )
    list_threads.append( t )

# start threads
for t in list_threads:
    t.start()

while running:
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass
    with lock:
        screen.blit( surface, (0,0) )# draw the surface on the screen

    pygame.display.flip()
    pygame.display.update()# update the display

    clock.tick(FPS) 
    #quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


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