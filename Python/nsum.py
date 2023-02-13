""" n=int(input("Enter number here: "))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum) """
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   while(num > 0):  
       sum += num  
       num -= 1 
print("The sum is",sum)  