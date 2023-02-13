num=int(input("Enter number here: "))
li=[int(i) for i in str(num)]
n=len(li)
m=0
for i in li:
    m=m+i**n
print(m)
