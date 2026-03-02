import re
txt=input()
x=re.search("^[0-9]+$",txt)
if x:
    print("Match")
else:
    print("No match")