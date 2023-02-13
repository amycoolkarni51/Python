m = int(input("Enter a number ::")) #5
k = m - 1                           #4=k
for i in range(1,m+1):      
    for j in range(1,k):
        print(end="")
        k-=1
    for j in range(1,i+1):
        print("* ",end=" ")
    print("\r")
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(" ",end=" ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()