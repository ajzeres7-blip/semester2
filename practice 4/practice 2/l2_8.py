n=int(input())
a=1
lst=[]
while a<=n:
    lst.append(a)
    a*=2
for x in lst:
    print(x, end=" ")
