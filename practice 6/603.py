n=int(input())
lst=list(map(str,input().split()))
result=list(enumerate(lst))
for i in result:
    print(f'{i[0]}:{i[1]}', end=' ')