# Method 1- By using a temporary variable, temp

# num1 = input("Enter Num1:")
# num2 = input("Enter Num2:")
# print("Value of Num1 before swapping:",num1)
# print("Value of Num2 before swapping:",num2)
# temp = num1
# num1 = num2
# num2 = temp
print("*******************")    
# print("Value of Num1 after swapping:",num1)
# print("Value of Num2 after swapping:",num2)

#Without using a temporary variable

num1 = input("Enter Num1:")
num2 = input("Enter Num2:")
num3 = input("Enter Num3:")
print("Value of Num1 before swapping:",num1)
print("Value of Num2 before swapping:",num2)
print("Value of Num3 before swapping:",num3)
num1,num2,num3 = num2,num3,num1
print("*******************")
print("Value of Num1 after swapping:",num1)
print("Value of Num2 after swapping:",num2)
print("Value of Num3 after swapping:",num3)
