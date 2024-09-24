#Example

# print("this is the starting point")
# print("this is the starting point")
#
# try:
#     print(x)
# except:
#     print("Exception occured")
#
# print("this is the end point")
# print("this is the end point")

#Example

# print("this is the starting point")
# print("Program start")
#
# try:
#     print(10/2)  #5
# except:
#     print("Exception occured..Handled..")
# print("Program Completed")
#
# #Example
#
# print("this is the starting point")
# print("Program start")
#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception occured..Handled..")
# print("Program Completed")

#Example:Multiple except block - try,except else ,finally

# try:
#     num1,num2 = 10,0
#     result = num1/num2
#     print("Result is...",result)
#
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception")
# except SyntaxError:
#     print("Thrown SyntaxError exception ")
# except:
#     print("Exception Handled")
# else:
#     print("No exception occured")
# finally:
#     print("Always excuted...")

#Example:Raising your own exception


def integer(num):
    if num==0:
        raise ValueError("only integer value are allowed")
    if num%2==0:
        print("number is even")
    else:
        print("Number is odd")

print("Checking number is even or odd by calling function...")
num=-1
try:
    integer(num)
except ValueError:
    print("Value error occurred and handled")
print("Program completed")