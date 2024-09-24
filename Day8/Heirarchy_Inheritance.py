#Heirarchy Inheritance

#Example

class A:     #Parent Class
    x,y = 10,20
    def add(self):
        print(self.x+self.y)

class B(A):   #Child Class of A
    a,b = 200,100
    def sub(self):
        print(self.a-self.b)

class C(A):   #Child Class of A
    i,j = 2,5
    def mul(self):
        print(self.i*self.j)

bobj=B()
bobj.add()  #30
bobj.sub()  #100

cobj=C()
cobj.add()  #30
cobj.mul()   #10