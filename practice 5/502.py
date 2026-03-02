import re
S=input()
P=input()
x=re.search(rf"{P}",S)
if x:
    print("Yes")
else:
    print("No")
