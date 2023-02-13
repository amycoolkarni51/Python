import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
y = arr1.view()
arr1[0] = 42

print(arr1)
print(y)
counter = 3

while counter <= 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')