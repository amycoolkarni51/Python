n = int(input("Enter a number :: "))
j=65
for i in range(n):
    for k in range(i+1):
        print(chr(j),end=" ")
    j+=1
    print()
rows = int(input("Enter number of rows:: "))
ascii_value = 65
for i in range(rows):
    for space in range(1, (rows-i)+1):
        print(end=" ")
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("")
n = int(input("Enter a number :: "))
k=65
for i in range(1,n+1):
    for space in range(1, (n-i)+1):
        print(end=" ")
    for j in range(1,i+1): 
        print(chr(k),end=" ")
        k+=1
    print()
m=int(input("Enter number here:: "))
k=65
for i in range(1,m+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()
