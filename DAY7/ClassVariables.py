# Example: Class Variables

class Myclass():

    a,b = 10,20  #class variables

    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=Myclass()
mc.add()  #30
mc.mul()  #200

#Example: Combination of Global,Class and Local Variables

i,j = 15,35  # i & j are global variables

class Myclass():
    a,b = 10,20  #a & b are Class variables

    def add(self,x,y):   #x & y are Local variables
        print(x+y)
        print(self.a+self.b)  #30
        print(i+j)  #50

mc=Myclass()
mc.add(100,200)  #300

# Example : Variables name are same for all 3 variables

a,b = 10,40  #Global variables

class MyClass():
    a,b = 10,80  # Global variables

    def add(self,a,b):
        print(a+b)   #Local Variables
        print(self.a+self.b)  #90
        print(globals()['a']+globals()['b'])    #  50 Calling Global Variables

mc=MyClass()
mc.add(200,20)  #220

# Example : One Class can have multiple objects

class MyClass:
    def display(self,name):
        print("This is a Instance....")
        print(name)

obj1=MyClass()
obj1.display("John")

obj2=MyClass()
obj2.display("Scott")