# A dictionary is a collection which is unordered , mutable (changeable) and indexed.
# In python, it is written with curly brackets, and they have keys and values.

# Example : Creating dictionary

mydict = {101 :"x",102:"y",103:"z"}
print(mydict)

# Example : Accessing item from the dictionary

mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}
print(mydict["brand"])  #hyudai
print(mydict["model"])  #110

# Using get()

x = mydict.get("year")
print(x)  #2021

#Example :hange values in dictionary
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}
print(mydict)  #{'brand': 'hyudai', 'model': '110', 'year': 2021}
mydict["year"] = 2023
print(mydict)  #{'brand': 'hyudai', 'model': '110', 'year': 2023}

#Example : Readiing item from dictionary using loop

mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}

for i in mydict:
    print(i)  #print only keys from dictionary

for i in mydict:
    print(mydict[i]) #print only values from dictionary

for i in mydict.values():
    print(i)  #print only values from dictionary

for x,y in mydict.items():
    print(x,y)  #print keys along with the values from dictionary

#Example : Check key is exist in dictionary or not
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}

if "model" in mydict:
    print("Exist")
else:
    print("Not Exist")

print("year" in mydict)  #True

# #Example : Find number of item in dictionary
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}
print(len(mydict))  #3

#Example : Adding items to dictionary
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}
mydict["color"]="red"
print(mydict)  #{'brand': 'hyudai', 'model': '110', 'year': 2021, 'color': 'red'}

# #Example : Remove items to dictionary
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}

mydict.pop("year")
print(mydict)  #{'brand': 'hyudai', 'model': '110'}

del mydict["brand"]
print(mydict)  #{'brand': 'hyudai', 'model': '110'}

del mydict
print(mydict)  #NameError: name 'mydict' is not defined

mydict.clear()
print(mydict)  #{}

#Example : copying items into dictionary
mydict = {
    "brand":"hyudai",
    "model":"110",
    "year":2021
}

mydict1 = mydict
print(mydict1)  #{'brand': 'hyudai', 'model': '110', 'year': 2021}

# Using copy()

mydict1 = mydict.copy()
print(mydict1)  #{'brand': 'hyudai', 'model': '110', 'year': 2021}


