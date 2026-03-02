import re
txt='SomeTypeOfCase'
x=re.sub(r'([a-z])([A-Z])',r'\1 \2',txt) #rewrite the string by adding space between 2 groups found
print(x)