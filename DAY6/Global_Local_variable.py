# Global variables : Variable created outside of the function
# Local variables : Variable created inside of the function

#Example
global_var = 20   #Global variable

def func():
    local_var = 10   #local variable
    print(global_var)
    print(local_var)
func()

print(global_var)  #Valid bcoz global_var is global variable of func()  (20)
# print(local_var)  #Invalid bcoz local_var is local variable of func() (NameError: name 'local_var' is not defined)


#Example:

xy = 100  #global

def cool():
    xy=200  #local
    print(xy)

cool()  #200 if global and local variable name is same so the function only call the local variable

#Example: Using global variable in local variable and update the value

xy =100 #global

def cool():
    global xy
    xy =200  #global
    print(xy)

cool()  #200
print(xy)  #200

#Example: Create global variable inside the function so we have to use global keyword.

def cool():
    global x
    x =  100
    print(x)
cool()  #100
print(x)  #100 able to access x bcoz,it is global variable

