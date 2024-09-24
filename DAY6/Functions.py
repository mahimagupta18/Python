# Function means set of statements which will perform a task
# 1)Function declaration/reactions
# 2)Calling the function invoking function

# def --> create function
# functionname() --> function call
# 1)Function does not take arguments not return any values(None)
# 2)Function does not take arguments but return some value
# 3)Function take arguments but no return value
# 4)Function take arguments and also return value


#Example: With argument

def myfun(name):
    print("Hello..",name)
myfun("Mahima")   #Hello.. Mahima

#Example : With two argument

def cal(a,b):
    return(a+b)

sum=cal(100,200)
print(sum)  #300

#Example :

def func():
    return
print(func())  #None

def func():
    i=10
print(func())  #None

#Example:
def cal(a,b):
    print(a+b)
cal(10,20)  #30

def func(a,b):
    return(a+b)
print(cal(1000,20))  #1020