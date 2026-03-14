def fun(N):
    cnt=1
    while cnt**2<=N:
        yield cnt**2
        cnt+=1
inp=int(input())
lst=fun(inp)
for i in lst:
    print(i, end=" ")
    