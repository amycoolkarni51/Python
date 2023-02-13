#Write a python program to create numpy array and add, delete element in array
import numpy as np
number=np.array([5,7,19,20,5,6,8])
print(number)
num1=np.delete(number,6)
print(num1)
num2=np.append(number,20)
print(num2)