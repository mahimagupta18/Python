#Overriding Method : overriding method allows a child class to provide a specific
#implementation of a method that is already provided by one of its parent classes.

#Super Keyword : It invoke the parent class method through the child class method

# Example : calling parent class method using child class (super())
#
# class A:   #Parent class
#     def m1(self):
#         print("this is a m1 Method of A ")
#
# class B(A):  #Child Class
#     def m1(self):
#         print("this is a m2 Method of B")
#         super().m1()
#
# bobj=B()
# bobj.m1()  #this is a m2 Method of B
#            #this is a m1 Method of A

#Example:
#
# class A:
#     x,y = 10,20  #class variable
#
# class B(A):
#     i,j=100,200    #class variable
#     def add(self,a,b):    #local variable
#         print(a+b)             #3000
#         print(self.i+self.j)   #300
#         print(self.x+self.y)   #30
#
# bobj=B()
# bobj.add(1000,2000)

#Example : how to poverriding variables

# class Parents:
#     name = "John"
#
# class Child(Parents):
#     name = "Mahima"   #overriding the variable value
#     def test(self):
#         print(super().name)
#
# obj = Child()
# # print(obj.name)   #Mahima

#Example : Overriding methods

class Bank:
    def rateofinterest(self):
        return 0

class XBank(Bank):
    def rateofinterest(self):
# obj.test()   # John
        return 10

class YBank(Bank):
    def rateofinterest(self):
        return 12

x=XBank()
print(x.rateofinterest())  #10

y=YBank()
print(y.rateofinterest())  #12
