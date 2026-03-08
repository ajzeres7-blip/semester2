n=int(input())
lst=list(map(int,input().split()))
x=all(x>=0 for x in lst)
if x:
    print('Yes')
else:
    print('No')