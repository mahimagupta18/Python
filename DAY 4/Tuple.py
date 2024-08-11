# how to create Tuple

mytuple = (1 ,2 ,3 ,4 ,5)
mytuple1 = ("apple","banana","orange")
print(mytuple)
print(mytuple1)
mytuple = tuple()  #empty

# Example : accessing the element from the tuple

mytuple = ("apple","banana","orange","cherry")
print (mytuple[2])  #orange
print (mytuple[-2])  #orange

# Example : Range of indexes

mytuple = ("apple","banana","orange","cherry","kiwi","grapes","melon")

print(mytuple[2:6])   #('orange', 'cherry', 'kiwi', 'grapes')
print(mytuple[-3:-1])  #('kiwi', 'grapes')

# Example : Changing tuple items
#by default tuple does not allow you to change the value bcoz,it is immutable
#but there is work around
#tuple --> list(modify) --> tuple

#mytuple = ("apple","banana","orange","cherry")

mytuple1 = ('Kiwi',100,200)
mylist =list(mytuple)
mylist[1] = 300
mytuple = tuple(mylist)
print(mytuple)  #('apple', 300, 'orange', 'cherry')

# Example : Reading tuple items using loop

mytuple = ("apple","banana","orange","cherry")

for i in mytuple:
    print(i)

#Example : Check if the item is exist in the tuple or not

mytuple = ("apple","banana","orange","cherry")
if 'cherry' in mytuple:
    print("Yes, Cherry is present")
else:
    print("No, Cherry is not present")

# Example : Tuple length  (counting number of items in a tuple)

mytuple = ("apple","banana","cherry","kiwi","orange")
print(len(mytuple))  #5

#Example : Add items to tuple - not possible or cannot change the values

# mytuple = ("apple","banana","orange","cherry")
# mytuple[1] = 'kiwi'   #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

# Example : copy tuple

mytuple = ("apple","banana","orange","cherry")
mytuple2 = mytuple
print(mytuple2)  #('apple', 'banana', 'orange', 'cherry')

# Example : remove items from the tuple - not possible bcoz it is immutable

mytuple = ("apple","banana","orange","cherry")
#mytuple.remove("apple")  #invalid (it is not possible)
# del mytuple
# print(mytuple)  #NameError: name 'mytuple' is not defined

#Example : combine/join tuple
mytuple = ("apple","banana","orange")
mytuple1 = (1 ,2 ,3 ,4)
mytuple3 = mytuple + mytuple1
print(mytuple3)  #('apple', 'banana', 'orange', 1, 2, 3, 4)

#Example : comparasion of tuple
mytuple = ("apple","banana","orange")
mytuple1 = (1 ,2 ,3 ,4)

if mytuple == mytuple1:
    print("Equal")
else:
    print("Not Equal")

