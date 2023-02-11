def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Enter operation: ")
print("i.Add")
print("ii.Subtract")
print("iii.Multiply")
print("iv.Division")
select=input("Enter operation i/ii/iii/iv : ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if select=='i':
    print(num1,"+",num2,"=",add(num1,num2))
elif select=='ii':
    print(num1,"+",num2,"=",sub(num1,num2))
elif select=='iii':
    print(num1,"+",num2,"=",mul(num1,num2))
elif select=='iv':
    print(num1,"+",num2,"=",div(num1,num2))
else:
    print("Invalid input")
