#Factorial Number with Iterative Method
#5! = 1 * 2 * 3 * 4 * 5 = 120

factorial = 1
num = 5

if num < 0:
    print("Factorial does not exist for negative number")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("The factorial of " , num , "is", factorial)

#Factorial Number with Recursive Function

def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of  " ,num ,"is", factorial(num))

#Factorial Number with Ternary operator

def factorial(n):
    return 1 if(n==0) or (n==1) else n*factorial(n-1)
num=5
print("Factorial of ",num ,"is", factorial(num))