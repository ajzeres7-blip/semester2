import re
txt=input()
x=re.findall(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]',txt)
print(len(x))