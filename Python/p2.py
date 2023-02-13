def isPrime(n, i = 2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return isPrime(n,i+1)
n=int(input("Enter number here: "))
if isPrime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
     