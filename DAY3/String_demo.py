

#Example 1 : Ways of creating string variable

s='Welcome'
s=("Welcome")
s = str('Welcome')
s = str("Welcome")

#Creating empty string variables
name =""
name =''
name = str()

#Example 2 : Ways of creating string variable

#mutable - cannot change the value of variable
#immutable - van change the value of variable
#String is immutable
#if the value is change after updation then it is immutable
str1 = 'Welcome'
print(id(str1))  #2044950658336

str1 = str1 + 'to Python'
print(id(str1))   #3229893672880

#Example 3 : + and * with string

str = 'Welcome'

print(str + 'Programming')  #WelcomeProgramming  (+ concatenation/joining)

print(str*3)  #WelcomeWelcomeWelcome   (* print multiple times)

#Example 4 : Slicing
#starting index 0
#Ending index 1

str = "Welcome"
print(str[1:3])  #el
print(str[:4])  #Welc
print(str[2:])  #lcome

print(str[1:-1])  #elcom Last 1 character remove
print(str[1:-2])  #elco Last 2 character remove

#Example 5 : ord() and chr()

print(ord('B')) #66 return the ASCII code of the character
print(chr(65))  #A return character represent by a ASCII number

#Example 6 : max(), min(), len()

print(max('abc'))   #c
print(min('abc'))   #a
print(len('welcome')) #5

#Example 7 : in and not in operator  - return true/false
s='welcome'

print('come' in s)  #True
print('lome' in s)  #False

print('come' not in s)  #False
print('lome' not in s)  #True

#Example 8 : String comparison

print("tim" == "tie")  #False
print("free" != 'freedom')  #True
print('arrow' > 'aron') #True
print("right" >= "left")  #True
print('teeth' < 'tee')  #False
print("yellow" <= "fellow")  #False
print("abc" > " ")  #True
print("**********")

#Example 9 : Testing strings
s = 'Welcome to Python'
print(s.isalnum())  #false
print ('welcome'.isalnum())  #True
print("2012".isdigit())  #True
print('first number'.isidentifier())  #false
print(s.islower())  #False
print("WELCOME".isupper())  #True
print(" ".isspace())  #True
print("**********")

#Example 10 : Searching for substring
s = "welcome to python"

print(s.endswith("thon"))  #True
print(s.startswith("good"))  #False
print(s.find("to"))  #8 (position of the starting character)
print(s.find("become"))  #-1
print(s.count("t"))  #2(how much time its come in the given string)
print("*******")

#Example 11 : Converting string
s = "String in PYTHON"

s1 = s.capitalize()
print(s1)  #String in python

s2 = s.title()
print(s2)   #String In python

s3 = s.lower()
print(s3)  #string in python

s4 = s.replace("in", "on")
print(s4)  #strong on python

s5 = s.upper()
print(s5)  #STRING IN PYTHON

#Example 12 :REverse a string
#Method1:

s = "Welcome"
rev_str = ""
for i in s:
    rev_str = i+rev_str
print(rev_str)

#Method2:
s = "Python"
rev_str = s[::-1]
print(rev_str)