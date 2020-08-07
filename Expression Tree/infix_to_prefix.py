class infix_to_prefix:
    precedence={'+':3,'&':3,'(':2,')':1}
    def __init__(self):
        self.items=[]
        self.size=-1
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
    def is0perand(self,i):
        List_op = []
        for a in range(1000):
            List_op.append('I'+str(a))
        if i in List_op:
            return True
        else:
            return False
    def reverse(self,expr):
        rev=[]
        for i in expr:
            if i == '(':
                i=')'
            elif i == ')':
                i='('
            rev.insert(0,i)
        return rev
    def infixtoprefix (self,expr):
        prefix=""
        for i in expr:
            if(self.is0perand(i)):
                prefix +=i
            elif(i == '!'):
                prefix+=i
            elif(i in '+&'):
                while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
                    prefix+=self.pop()
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop()
                while o!='(':
                    prefix +=o
                    o=self.pop()
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                prefix+=self.pop()
        return prefix
    def lock_I(self,expr):
        exprl = []
        wait = ''
        for i in expr:
            if i == 'I':
                wait = i
            else:
                wait+= i
                exprl.append(wait)
                wait = ''
        return exprl

solve=infix_to_prefix()
expr = "(((I0&I1&!I2)+!I1)+I3)"
rev = ''
exprl = solve.lock_I(expr)
rev=solve.reverse(exprl)
result=solve.infixtoprefix(rev)
result = solve.lock_I(result)
if (result!=False):
    prefix=solve.reverse(result)
    prefixsolve =''
    for i in prefix:
        prefixsolve+=i
    print("the prefix expr of :",expr,"is",prefixsolve)
