class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person(input("Enter Name: "),input("Enter Age: "))
print("My name is ", p1.name)
print("My Age is ",p1.age)