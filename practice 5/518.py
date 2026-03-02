import re
S=input()
P=input()
pattern=re.escape(P)
x=re.findall(rf'{pattern}', S)
print(len(x))