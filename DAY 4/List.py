# how to create list

mylist1 = [1 ,2 ,3 ,4 ,5]
mylist2 = ["apple","banana","orange"]
mylist3 = [1 ,"apple",4 ,"grapes"]
mylist = list()  #empty

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

# Example : accessing the element from the list

mylist = ["apple","banana","orange"]
print(mylist[0])
print(mylist[1])
print(mylist[-1])   #Negative index is allowed in list and it take last element from the list.
print(mylist[-2])

# Example : Range of indexes

mylist = ["apple","banana","orange","cherry","kiwi","grapes","melon"]
print(mylist[2:6])   #['orange', 'cherry', 'kiwi', 'grapes']
print(mylist[-5:-1]) #['orange', 'cherry', 'kiwi', 'grapes']

# Example : Change list values

mylist = ["apple","banana","orange"]
print(mylist)
mylist[0] = "cherry"
print(mylist)

#Example : Read the elements using loop

mylist = ["apple","banana","orange","cherry","kiwi","grapes","melon"]
for i in mylist:
    print(i)

#Example : Check if the item is exist in the list or not

mylist = ["apple","banana","orange"]
if "apple" in mylist:
    print("Yes.. apple is present")
else:
    print("No.. apple is not present")

# Example : List length  (counting number of items in a list)

mylist = ["apple","banana","orange"]
print(len(mylist))  #3

#Example : Add items append() insert()

mylist = ["apple","banana","orange"]
mylist.append("Cherry")  #adding new item at the end of the  list
print(mylist)   #['apple', 'banana', 'orange', 'Cherry']

mylist.insert(2,"melon")  #add item some where in the middle of the list based on the index
print(mylist)   #['apple', 'banana', 'melon', 'orange', 'Cherry']

# Example : remove items from the list

# pop() function - here we should specify index not the value
mylist = ["apple","banana","orange"]
mylist.pop(1)
print(mylist)  #['apple', 'orange']

#del keyword - here del command removes single item based on the index
mylist = ["apple","banana","orange"]
del mylist[0]
print(mylist)  #['banana', 'orange']

#clear() function  - here remove all the values from the list
mylist = ["apple","banana","orange"]
mylist.clear()
print(mylist)  #[]

# Example : copy list

#list()
mylist1 = ["apple","banana","orange"]
mylist2 = list(mylist1)

print(mylist1)  #['apple', 'banana', 'orange']
print(mylist2)  #['apple', 'banana', 'orange']

#copy()
mylist1 = ["apple","banana","orange"]
mylist2 = mylist1.copy()

print(mylist1)  #['apple', 'banana', 'orange']
print(mylist2)  #['apple', 'banana', 'orange']

#Example : combine/join lists

# #using + operator
list1 = ["a" ,"b" ,"c"]
list2 = [1 ,2 ,3 ,4]
list3 = list1 + list2
print(list3)  #['a', 'b', 'c', 1, 2, 3, 4]

#using loop statement
list1 = ["a" ,"b" ,"c"]
list2 = [1 ,2 ,3 ,4]
for i in list2:
    list1.append(i)
print(list1)   #['a', 'b', 'c', 1, 2, 3, 4]

#using extend() function
list1 = ["a" ,"b" ,"c"]
list2 = [1 ,2 ,3 ,4]
list1.extend(list2)
print(list1)   #['a', 'b', 'c', 1, 2, 3, 4]
