import re
txt=input()
x=re.search("cat|dog", txt)
if x:
    print("Yes")
else:
    print("No")
