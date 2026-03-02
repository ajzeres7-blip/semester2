import re
txt=input()
x=re.findall(r'[0-9][0-9]+',txt)
if x:
    print(*x)
else:
    print("\n")