import re
txt='SomeTypeOfCase'
x=re.findall(r'([A-Z][a-z]*)',txt) 
print('_'.join(x))