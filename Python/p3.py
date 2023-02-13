num=int(input("Enter number here: "))
sum=0
for i in range(1,num):
    if  num%i ==0:
        sum=sum+i
if sum==num:
    print(num,"is a perfect number")
else:
    print(num,"is not perfect number")