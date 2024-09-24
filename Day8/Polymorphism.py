#Polymorphism means one thing have many forms and we can implement using overloading method
# Shape .... Circle,rectangle,Square
# add(10)
# add(10,20)
# add(10,20,30)

#Example : Polymorphism (overloading)

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello"+ name)
        else:
            print("Hello")


h=Human()
h.sayhello("Mahima")
h.sayhello()

#Example

class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

c=calculation()
c.add()   #0
c.add(10,20)  #30
c.add(100,200,300)  #600