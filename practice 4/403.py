def fun(n):
    cnt=0
    yield cnt
    while cnt<=n:
        cnt+=1
        if cnt%3 == 0 and cnt%4 == 0:
            yield cnt
inp=int(input())
for i in fun(inp):
    print(i, end=" ")
