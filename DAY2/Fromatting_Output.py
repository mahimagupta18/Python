name ='John'
age =20
sal =8000
name,age,sal='John',20,8000

# Approach 1
print(name)
print(age)
print(sal)
print(name,age,sal)

# Approach 2
print("Name is :",name)
print("Age is :",age)
print("Salary is :",sal)

#Approach 3

print("Name is :%s Age is:%d Salary is:%g" %(name,age,sal))

#Approach 4

print("Name is :{} Age is :{}  Salary is :{}" .format(name,age,sal))
print("Age is :{} Name is :{}  Salary is :{}" .format(age,name,sal))