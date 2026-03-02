import re
txt=input()
x=re.search(r"Name: (.*?), Age: (.*)",txt)
if x:
    print(f'{x.group(1)} {x.group(2)}')