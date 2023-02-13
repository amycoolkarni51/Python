import re
reg=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
    if(re.fullmatch(reg,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
if __name__=='__main__':
    email=input("Enter Email Here: ")
    check(email)
string="Hello I live on street 9 which is near 45 street 23"
print(re.findall(r"\d",string))