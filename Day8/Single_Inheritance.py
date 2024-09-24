#Single Inheritance

#Example 1:

class A:  #Parent Class
    def m1(self):
        print("this is a class A")

class B(A):   #Child Class
    def m2(self):
        print("this is a class B")

bobj=B()
bobj.m1()   #this is m1 method from class A but access through class B
bobj.m2()   #this is m2 method from class B


#Example 2 :

class A:     #Parent Class
    x,y = 10,20
    def add(self):
        print(self.x+self.y)

class B(A):   #Child Class
    a,b = 200,100
    def sub(self):
        print(self.a-self.b)

bobj=B()
bobj.add()  #30
bobj.sub()  #100
