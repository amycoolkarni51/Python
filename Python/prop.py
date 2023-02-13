import re
mstr="My number is +91-273849456"
patt= re.compile(r'\+91')
match=patt.finditer(mstr)
for x in match:
    print(x)

cities=('pune','mumbai')
continent='Asia'
dict1=dict.fromkeys(cities,continent)
print(dict1)


