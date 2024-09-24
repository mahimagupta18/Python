#Example: Write a data into text file
#
# file=open("D:\Python\Demofiles\myfiles.txt",'w')
# file.write("this is 1 statement...\n")
# file.write("this is 2 statement...\n")
# file.write("this is 3 statement...\n")
# file.write("this is 4 statement...\n")
# file.write("this is 5 statement...\n")
# file.close()
# print("Program completed")

#Example: Reading a data into text file

# file=open("D:\Python\Demofiles\myfiles.txt",'r')
# print(file.read())
# file.close()

#Example: Appending an data into text file

file=open("D:\Python\Demofiles\myfiles.txt",'a')
file.write("this is 6 statement...\n")
file.write("this is 7 statement...\n")
print("Program is completed")
file.close()
