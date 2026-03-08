n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(zip(A,B))
result=0
for i in C:
    result+=i[0]*i[1]
print(result)