def outer(a,b):
    pass
    def inner(a,b):
        return a+b
    add=inner(a,b)
    return add + 5
m=int(input("Enter number: "))
n=int(input("Enter number: "))
result=outer(m,n)
print(result)