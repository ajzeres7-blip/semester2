def down(n):
    while n>=0:
        yield n
        n-=1
inp=int(input())
for i in down(inp):
    print(i)