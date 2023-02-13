def findSum(n):
    if n<=1:
        return n
    else:
        return n + findSum(n-1)
m=int(input("Enter number: "))
print(findSum(m))
