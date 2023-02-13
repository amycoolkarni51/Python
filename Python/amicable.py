num1=int(input("enter a number: "))
sum1=0
for i in range(1,num1):
    if num1%i==0:
       sum1=sum1+i
num=int(input("enter a number: "))
sum2=0
for j in range(1,num):
    if num%j==0:
        sum2=sum2+j
if sum1==num and sum2==num1:
    print("Numbers are Amicable") 
else:
    print("Numbers not are Amicable") 