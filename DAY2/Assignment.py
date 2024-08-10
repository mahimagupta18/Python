#1 Check the given number is positive or negative

num=1
if num>=1:
    print("Number is Positive")
else:
    print("Number is Negative")


#2 Check the largest of 2 number

num1 =100
num2 =20
if num1>num2:
    print("num1 is greater than num2")
else:
    print("num1 is not greater than num2")

#3 check the largest of 3 number

a =10
b =90
c =50
if a>b:
    print(" a is greater than b")
elif a>c:
    print("a is greater than c")
else:
    print("b is greater than c")

#4 Print week number if you provide weekname as input

weekname = input("Enter Week Name:")

if weekname == 'Sunday':
    print(1)
elif weekname == 'Monday':
    print(2)
elif weekname == 'Tuesday':
    print(3)
elif weekname == 'Wednesday':
    print(4)
elif weekname == 'Thursday':
    print(5)
elif weekname == 'Friday':
    print(6)
else:
    print(7)


