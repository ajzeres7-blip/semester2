def printer(t,lst):
    cnt=1
    while cnt<=t:
        for i in lst:
            yield i
        cnt+=1
lst_=list(map(str,input().split()))
n=int(input())
print((' ').join(printer(n,lst_)))