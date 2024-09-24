# 2 Types of arguments / parameters we can passs to the function
# 1)Positional Arguments
# 2)keyword arguments

#Example :

def func(i,j):
    print(i,j)
func(10,20) #positional
func(i=10,j=20)  #Keyword

#Example :Default values assigned to positional arguments

def func(i,j=100):
    print(i,j)
func(10,200) #10 200
func(800)  #800 100

#Example:Keywords arguments

def greetings(name,greetmsg):
    print(greetmsg +" "+name)
greetings(name = "Mahima",greetmsg="Hello")  #Hello Mahima
greetings(greetmsg="Hey",name="Mahima")  #Hey Mahima

#Example:Combination of both argumnets

def myfunc(a,b,c):
    print(a,b,c)
myfunc(10,20,30)  #positional 10 20 30
myfunc(a=20,b=80,c=10)  #keyword 20 80 10

myfunc(10,20 ,c=30) #10 20 30
myfunc(10,b=20,c=30) #10 20 30

# myfunc(10,b=60,50)  #this is wrong as positional argument must appear before any keyword argument
# myfunc(10,20,b=30) #this is having logical error


#Example:function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(200,100))  #(200,100)
print(largest(10,20))  #(10,20)

res = largest(10,20)
print(res)  #(20,10)


