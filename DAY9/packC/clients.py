import sys

sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\packA")
sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\packB")

#Approach
import emp
empobj = emp.Employee(101,"John",100000)
empobj.displayemp()

import stu
stuobj = stu.Student(1001,"Scott",'B')
stuobj.displaystu()

#Approach

from emp import Employee
empobj=Employee(102,"Jerry",200000)
empobj.displayemp()

from stu import Student
stuobj = Student(1002,"Tom",'A')
stuobj.displaystu()