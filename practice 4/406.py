def fibonacci(n):
    a, b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
inp=int(input())
result=list(fibonacci(inp))
print((', ').join(map(str, result)))