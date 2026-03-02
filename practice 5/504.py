import re
txt=input()
x= re.findall(r'\d',txt)
if x:
    print(*x, sep=" ")
else:
    print("\n")