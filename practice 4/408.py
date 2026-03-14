def prime(n):
    cnt=2
    while cnt<=n:
        if all(cnt%i!=0 for i in range(2,cnt)):
            yield cnt
        cnt+=1
inp=int(input())
for i in prime(inp):
    print(i, end=' ')