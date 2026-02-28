n=input()
lst=list((map(int,input().split())))
amin=min(lst)
amax=max(lst)
for i in range(len(lst)):
    if lst[i]==amax:
        lst[i]=amin
for x in lst:
    print(x, end=" ")
    