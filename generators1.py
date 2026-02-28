def fun(N):
    cnt = 1
    while cnt**2 <= N:
        yield cnt**2
        cnt += 1
inp=int(input())
ctr = fun(inp)
for n in ctr:
    print(n)