def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))
#Balance
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

