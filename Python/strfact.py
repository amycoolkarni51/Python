""" n=int(input("Enter number here: "))
sum=1
for i in range(1,n+1):
    sum=sum*i
print(sum)
 """
my_sum=0
my_num = int(input("Enter number here: "))
temp = my_num
while(my_num):
   i=1
   fact=1
   remainder = my_num%10
   while(i<=remainder):
      fact=fact*i
      i=i+1
   my_sum = my_sum+fact
   my_num=my_num//10
if(my_sum == temp):
   print("The number is a strong number")
else:
   print("The number is not a strong number")