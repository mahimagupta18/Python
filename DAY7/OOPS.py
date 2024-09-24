#Example : Creating Class and object

class MyClass:    #Creating Class
    def myfun(self):    #creating  empty methods (self is for calling class)
        pass
    def display(self):  #creating methods
        print("John")
    def myfun1(self,name):   #Creating method with argument
        print(name)

mc = MyClass()   #Creating Object
mc.myfun()        #Calling Methods
mc.display()    #John
mc.myfun1("Scott")  #Scott

#Example :

class MyClass:
    def m1(self):
        print("this is an instance method...")
    @staticmethod     #Annotation of staticmethod
    def m2(self,num):     #In staticmethod self is considered as an argument
        print(self,num)

mc=MyClass()
mc.m1()
mc.m2(100,200)  #100 200   #Calling staticmethod using object is not standard way

MyClass.m2(10,20)  #10 20 here calling staticmethod directly using class not through object




