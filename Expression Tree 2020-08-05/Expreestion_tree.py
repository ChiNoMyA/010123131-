#----------------------------------------------------------------------
# this code for 010123131 Software Development Practice I
#   Class Assignment (2020-08-05)
#   Name : Gorrawe Srichainon 6201012620287
#   Cpr.E
#   
#   2020-08-05 problem1 Boolean Expression Tree
#   
#----------------------------------------------------------------------
#import zone
import random
import pygame
from pygame.locals import *
import sys
import string
import math 
#----------------------------------------------------------------------
#openfile
F = open("C:\\Users\\66912\\Desktop\\NewFloder\\Work\\VSCode\\python\\tester\\Calculator\\boolean expresstion\\expression_text_XXX.txt","r")
Flie_list = F.readlines()
FileStr = ''
for i in Flie_list:
    FileStr+=i
expression_list_file = FileStr.split('\n')
#----------------------------------------------------------------------
#variable
index = 5
expression =  expression_list_file[index]
scr_w,scr_h = 1600,900
Text_size = 60
FPS = 10
#expression_list = [ "(I0&I1 + !(I1&I2))" ,"!(1+0)","!(!(0+I0&1))","(I0+!I1+!(I2))&(!I0+I1+I2)","!(I0&I1)+!(I1+I2)","(((I0&I1&!I2)+!I1)+I3)"]
#expression =  expression_list[5]
#----------------------------------------------------------------------
#pygame start
pygame.init()
screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption('Expression Tree')
clock = pygame.time.Clock()
#----------------------------------------------------------------------
#ListOperation
List_op = []
for a in range(100):
    List_op.append(str(a))
    for b in string.ascii_letters:
        List_op.append(b+str(a))
for b in string.ascii_letters:
        List_op.append(b)
#----------------------------------------------------------------------
#Draw in pygame
class Draw:
    def __init__(self,x=0,y=0,rcir=0,rline=0,linewidth = 0,L_startX=0,L_startY=0,angel=0,text=0):
        #circle zone
        self.circlePos = (x,y)
        self.circleRadius = rcir
        #----------------------
        #line zone
        self.Rline =rline
        self.linewidth = linewidth
        self.StartLinePos = (L_startX,L_startY)
        self.angel = angel
        self.EndLinePos = (L_startX + int(rline * math.cos(math.radians(angel)) ),L_startY + int(rline * math.sin(math.radians(angel)) ))
        #----------------------
        #Text zone
        self.Text = text
        self.font = pygame.font.Font(None, Text_size)
        self.R = random.randint(0,255)   
        self.G = random.randint(0,255)
        self.B = random.randint(0,255)
        self.color = (self.R,self.G,self.B,255)
        self.color_text = self.color
        #self.color_line = self.color
        #self.color_circle = self.color_line
        #self.color_text = pygame.Color('navyblue')
        self.color_line = pygame.Color('steelblue')
        self.color_circle = self.color_line
        #----------------------
    def DrawCircle(self):
        pygame.draw.circle( screen, self.color_circle,self.circlePos, self.circleRadius )
    def DrawCirwithLine(self,line):
        self.circlePos = (self.circlePos[0] + int(line.EndLinePos[0] + self.circleRadius*math.cos(math.radians(line.angel))/2),self.circlePos[1] + int(line.EndLinePos[1] + self.circleRadius*math.sin(math.radians(line.angel))/2))
        self.DrawCircle()
    def DrawLine(self):
        pygame.draw.line(screen, self.color_line,self.StartLinePos,self.EndLinePos, self.linewidth )
    def DrawLinewithCir(self,circle,multi,const_x_stop = 0,const_y_stop = 0):
        self.StartLinePos = (circle.circlePos[0] + int(circle.circleRadius * math.cos(math.radians(self.angel))/2 ),circle.circlePos[1] + int(circle.circleRadius * math.sin(math.radians(self.angel))/2 ))
        self.EndLinePos = (self.StartLinePos[0] + (int(multi*self.Rline * math.cos(math.radians(self.angel))/2 )  + const_x_stop),self.StartLinePos[1] + (int(self.Rline * math.sin(math.radians(self.angel)) /2)           + const_y_stop))
        self.DrawLine()
    def DrawText(self,text,pos):
        text_surface = self.font.render(text, True, self.color_text)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        screen.blit(text_surface, text_rect)
#----------------------------------------------------------------------
#Expession Tree
class Tree:
    class STACK:
        def __init__(self):
            self.items = []
        def isEmpty(self):
            return self.items == []
        def push(self, item):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
        def peek(self):
            return self.items[-1]
        def size(self):
            return len(self.items)
        def show(self):
            print(self.items)
    class Node:
        def __init__(self, root):
            self.left = None
            self.right = None
            self.root = root
    def __init__(self,expression):
        self.precedence={'+':3,'&':3,'(':2,')':1}
        self.items=[]
        self.size=-1
        self.List_op = List_op
        self.prefix = ''
        self.expression = expression
        self.stack = self.STACK()
        self.ExTree = None
        self.order = []
        self.Rnode = 35
        self.line_lenght = 14
        self.line_linewidth = 20
    def push(self,value):
        self.items.append(value)
        self.size+=1
    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def isempty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]
    def isOperand(self,i):
        if i in self.List_op:
            return True
        else:
            return False
    def reverse(self,expression):
        rev=[]
        for i in expression:
            if i == '(':
                i=')'
            elif i == ')':
                i='('
            rev.insert(0,i)
        return rev
    def infix_prefix (self,expression):
        for i in expression:
            if self.isOperand(i):
                self.prefix +=i
            elif i == '!':
                self.prefix+=i
            elif i in '&+':
                while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
                    self.prefix+=self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop()
                while o!='(':
                    self.prefix +=o
                    o=self.pop()
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                self.prefix+=self.pop()
        print(self.prefix)
        return self.prefix
    def Lock_ap(self,expression):
        exprl = []
        wait = ''
        for i in expression:
            if i == expression[-1] :
                if wait != '':
                    exprl.append(wait)
                    wait=''
                exprl.append(i)
            elif i.isalpha():
                if wait != '':
                    exprl.append(wait)
                    wait=''
                wait = i
            elif i in '1234567890':
                wait+= i
                exprl.append(wait)
                wait = ''
            else:
                if wait != '':
                    exprl.append(wait)
                    wait=''
                exprl.append(i)
    
        return exprl
    def InfixToPrefix(self):
        lock = self.Lock_ap(self.expression)
        reverse = self.reverse(lock)
        preresult = self.infix_prefix(reverse)
        result = self.Lock_ap(preresult)
        self.prefix = self.reverse(result)
        return self.prefix
    def PrefixToExpresstionTree(self):
        for i in range(len(self.prefix)-1,-1,-1):
            Op = self.prefix[i]
            if self.isOperand(Op):
                self.stack.push(Op)
            elif Op is '!':
                a = self.stack.pop()
                Node = self.Node(Op)
                Node.left = a
                self.stack.push(Node)
            elif Op in '&+':
                a = self.stack.pop()
                b = self.stack.pop()
                node = self.Node(Op)
                node.left = a
                node.right = b
                self.stack.push(node)
        self.ExTree = self.stack.pop()
        return self.ExTree
    def maxDepth(self,node): 
        if node is None : return 0 
        elif type(node) == str :return 1
        else : 
            l_depth = self.maxDepth(node.left) 
            r_depth = self.maxDepth(node.right) 
            if (l_depth > r_depth): 
                return l_depth+1
            else: 
                return r_depth+1
    def CheckRoot(self,text,pos,circle,multi):
        if pos == 'L':
            lineangel = 135
        elif pos == 'R':
            lineangel = 45
        line = Draw(rline = self.line_lenght, angel = lineangel, linewidth = self.line_linewidth)
        
        line.DrawLinewithCir(circle,multi,const_y_stop=100)
        circleA = Draw(rcir = self.Rnode)
        circleA.DrawCirwithLine(line)
        TextA = Draw(text=text)
        TextA.DrawText(text,circleA.circlePos)
        return circleA
    def DrawNodeTree(self,multi,node,pos = 'root',circle = None): 
        if type(node) == str :
            self.order.append(node)
            text = node
            self.CheckRoot(text,pos,circle,multi)
        elif node: 
            self.order.append(node.root)
            text = node.root
            if pos == 'root' :
                x = scr_w//2
                y = int(0.1 * scr_h)
                circle = Draw(x=x,y=y,rcir=self.Rnode)
                circle.DrawCircle()
                TextB = Draw(text=text)
                TextB.DrawText(text,(x,y))
                self.DrawNodeTree(multi//2 ,node.left,'L',circle) 
                self.DrawNodeTree(multi//2 ,node.right,'R',circle) 
            else :
                circleA = self.CheckRoot(text,pos,circle,multi)
                self.DrawNodeTree(multi//2 ,node.left,'L',circleA) 
                self.DrawNodeTree(multi//2 ,node.right,'R',circleA) 
    def DrawExpressionTree(self):   
        depth  = self.maxDepth(self.ExTree)
        multi = pow(2, depth +2 ) 
        self.DrawNodeTree(multi,self.ExTree)
#----------------------------------------------------------------------
#Solve infix to Expresstion tree by prefix
solve = Tree(expression)
solve.InfixToPrefix()
solve.PrefixToExpresstionTree()
#----------------------------------------------------------------------
is_running = True
#----------------------------------------------------------------------
#pygame running
while is_running:
    clock.tick(FPS) 
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
        
    screen.fill((0,0,0))
    solve.DrawExpressionTree()
    pygame.display.flip()
    pygame.image.save(screen, "Expression"+str(index+1)+".jpeg")
pygame.quit()

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
    