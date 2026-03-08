n=int(input())
a=list(map(int,input().split()))
b=list()
for i in a:
    if i!=0:
        b.append(1)
print(sum(b))