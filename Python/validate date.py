from datetime import datetime

# initializing string
test_str = input("Enter Date: ")
format = "%d-%m-%Y"

# checking if format matches the date
res = True

# using try-except to check for truth value
try:
	res = bool(datetime.strptime(test_str, format))
except ValueError:
	res = False

# printing result
print("Does date match the format? : " + str(res))
