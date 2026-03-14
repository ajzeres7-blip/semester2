def power_of_2(n):
    cnt=0
    while cnt<=n:
        yield 2**cnt
        cnt+=1
inp=int(input())
for i in power_of_2(inp):
    print(i, end=' ')
