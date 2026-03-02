import re
txt=input()
x=re.findall("\w+",txt)
count=0
for i in x:
     if len(i)==3:
         count+=1
print(count)
