def squares(a,b):
    for i in range(a,b):
        yield i*i
    yield b*b
inp=list(map(int,input().split()))
for i in squares(inp[0],inp[1]):
    print(i)
