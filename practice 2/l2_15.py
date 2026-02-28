n=int(input())
atten=set()
for _ in range(n):
    name=input().strip()
    atten.add(name)
print(len(atten))