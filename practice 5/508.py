import re
S=input()
D=input()
x=re.split(rf'{D}',S)
print(
    ','.join(x)
)