l=int(input("Length:"))
b=int(input("Breadth:"))
area=1/2*l*b
print(area)
#Sum operator
x=int(input("num1: "))
y=int(input("num2: "))
z=int(input("num3: "))
sum=x+y+z
if x==y or x==z or y==z:
    sum=0
    print(sum)
else:
    print(sum)
num=x+y
if num in range(15,20):
    num=20
    print(num)
else:
    print(num)
if x == y or abs(x-y) == 5 or (x+y) == 5:
    print(True)
else:
    print(False)