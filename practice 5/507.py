import re
S=input()
P=input()
R=input()
y=re.sub(rf'{P}',R,S)
print(y)