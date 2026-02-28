a=input()
b=input()
c=input()
if(a.find(b.lower())!=-1):
    print(a.replace(b,c))
else:
    print(a)