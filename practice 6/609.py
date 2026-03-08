n=int(input())
a=list(map(str,input().split()))
b=list(map(str,input().split()))
key=input()
c=dict(zip(a,b))
x=False
for i, j in c.items():
    if i==key:
        x=True
if x:
    print(c[key])
else:
    print("Not found")
