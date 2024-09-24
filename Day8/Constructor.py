#Example: Using Constructor

# class MyClass:
#     def __init__(self):
#         print("This is constructor")
#     def m1(self):
#         print("Hello")
#     def m2(self,a,b):
#         return(a+b)
#
# mc=MyClass()  #invoke constructor automatically
# mc.m1()  # method we have call explicitly by using object
# print(mc.m2(10,20))  #30

#Example:

# class MyClass:
#     name = "John"
#     def __init__(self,name):  #constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("Tom")  #passing parameter to the constructor

#Example:
#Req : Emp
  #Constructor : eid,ename,sal
  #display() : print eid,ename,sal

# class Emp:
#
#     def __init__(self,eid,ename,sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1 =Emp(101,"John",10000)
# e1.display()   #101 John 10000
#
# e2=Emp(102,"David",20000)
# e2.display()  #102 David 20000

#Example: __Str__ Constructor

#Req : Emp
  #Constructor : eid,ename,sal
  #Constructor : print eid,ename,sal

class Emp:

    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def __str__(self):    #Only return the string value
        return(self.ename)

e1 =Emp(101,"John",10000)
print(e1)  #John


