""" num=int(input("enter a number"))
for i in range(1,num+1):
    if num%i==0:
       print(i,end=" ") """
num = int(input("Please enter any number: "))

for x in range(2, num + 1):
    if(num % x == 0):
        n = 1
        for y in range(2, (x //2 + 1)):
            if(x % y == 0):
                n = 0
                break
            
        if (n == 1):
            print(x,end=" ")