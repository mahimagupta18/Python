# A set is a collection which is unordered and unindexed.
# In python it are written with curly brackets.
# Set is mutable

#Example :creating set
myset = {"apple","banana","cherry"}
print(myset)

#Example : accessing item from set

myset = {"apple","banana","cherry"}
for i in myset:
    print(i)

#Example : value exist in set or not

myset = {"apple","banana","cherry"}
print("banana"  in myset)  #True
print("banana2" in myset)  #False

#Example : Add items to set
# add()- add single item
# update() - add multiple item

myset = {"apple","banana","cherry"}
myset.add("kiwi")
print(myset)  #{'banana', 'cherry', 'apple', 'kiwi'}

myset = {"apple","banana","cherry"}
myset.update(["kiwi","grapes"])
print(myset)   #{'grapes', 'apple', 'banana', 'cherry', 'kiwi'}

#Example : Find number of item in a set

myset = {"apple","banana","cherry"}
print(len(myset))  #3

#Example : Remove item from a set
# remove() or  discard()

myset = {"apple","banana","cherry"}
myset.remove("apple")
print(myset) #{'banana', 'cherry'}

# myset.remove("xyz")
# print("xyz")  #KeyError : xyz

myset.discard("banana")
print(myset) #{'apple', 'cherry'}

myset.discard("xyz")
print(myset)  #will not throw any error

#Example : Clear all item from set

# myset = {"apple","banana","cherry"}
# myset.clear()
# print(myset)  #set()
#
# del myset
# print(myset) #NameError : name "myset" is not defined

#Example :joining two sets - union() or update()

myset = {"apple","banana","cherry"}
myset1 = {1,2,3}
set2=myset.union(myset1)
print(set2)  #{1, 2, 3, 'cherry', 'banana', 'apple'}

# update()
myset = {"apple","banana","cherry"}
myset1 = {1,2,3}
myset.update(myset1)
print(myset)  #{1, 2, 3, 'cherry', 'banana', 'apple'}


