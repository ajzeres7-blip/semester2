import re
txt=input()
x=re.findall(r"^[a-zA-Z].*\d$",txt)
if x:
    print("Yes")
else:
    print("No")