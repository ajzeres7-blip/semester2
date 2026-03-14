def fun(n):
    cnt=0
    while cnt<=n:
        yield cnt
        cnt+=2
inp=int(input())
for i in fun(inp):
    print(i,end=" ")