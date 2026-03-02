import re
txt="Rob found a34x#z5b yesterday."
x=re.compile(r'a.*b').findall(txt)
print(x)