import re
txt=input()
x=re.compile(r"\w+").findall(txt)
print(len(x))
