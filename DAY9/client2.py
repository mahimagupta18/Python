#Approach

import sys

sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\Package1")
sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\Package1\Package2")

import module1
import module2

module1.display()
module2.show()

#Approach

import sys

sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\Package1")
sys.path.append(r"C:\Users\mahim\PycharmProjects\Python_Training\DAY9\Package1\Package2")
from module1 import *
from module2 import *

display()
show()