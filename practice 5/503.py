import re
S=input()
P=input()
x=re.findall(rf"{P}",S)
print(len(x))