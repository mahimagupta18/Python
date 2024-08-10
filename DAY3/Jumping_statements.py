#Break statement

for i in range(1,10):
    if i ==6:
        break
    print(i)   # 1....9
print("Program Exist!!!!")

#continue statement

for i in range(1,10):
    if i ==6:
        continue
    print(i)   # 1....9
print("Program Exist!!!!")


#continue statement multiple conditions

for i in range(1,10):
    if i==5 or i==7 or 1==9:
        continue
    print(i)   # 1....9
print("Program Exist!!!!")