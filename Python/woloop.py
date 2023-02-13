def nol(n):
    if n!=0:
        nol(n-1)
        print(n,end=" ")
    
m=int(input("Enter number here: "))
nol(m)
def printNos(initial, last):
    if(initial<=last):
        print("\n",initial,end=" ")
        printNos(initial+1,last)
printNos(1,10)