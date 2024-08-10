# conditionalStatements
# If  If...else  elif


#Example : Print the person is Eligible for vote
#age>=18

age = 29
if age>=18:
    print('Eligible for vote')
else:
    print('Not eligible for vote')

#Example 1

if False:
    print("True condition")
else:
    print("False condition")

#Example 2

if 1:
    print("one")
else:
    print("Not one")

#Exapmle 3 : Find the number is Even/Odd     (num%=0 - Even)

num = 13
if num%2==0:
    print("Given number is Even")
else:
    print("Given number is Odd")

#Example 4 : If else in single line (ternary operator)

num = 17
print("Even Number") if num%2==0 else print("Odd Number")

#Example 5 : If else - Multiple statements in single line (ternary operator)

a=4
{print("Hello"),print("Python")} if a>=10 else {print("Hey"),print("Java")}

#Example 6 : Multiple condition using elif

weekno =3

if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("Thrusday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Saturday")
else:
    print("Invaild week")