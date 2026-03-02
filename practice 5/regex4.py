import re
txt="Today is Monday"
x=re.compile(r'[A-Z]+[a-z]+').findall(txt)
print(x)