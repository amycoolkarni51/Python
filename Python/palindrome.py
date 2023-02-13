str1=input("Enter string here: ")
str1=str1.lower()
n=len(str1)
if n<2:
    print(str1,"is palindrome")
elif str1[0] == str1[n - 1]:
    print(str1,"is a palindrome")
else:
    print("Not a palindrome")