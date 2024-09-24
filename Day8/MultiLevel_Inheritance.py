#MultiLevel Inheritance

#Example

class A:     #Parent Class
    x,y = 10,20
    def add(self):
        print(self.x+self.y)

class B(A):   #Child Class of A or Parent class of C
    a,b = 200,100
    def sub(self):
        print(self.a-self.b)

class C(B):   #Child Class of B or A
    i,j = 2,5
    def mul(self):
        print(self.i*self.j)

cobj=C()
cobj.add()  #30
cobj.sub()  #100
cobj.mul()   #10