def fun(n):
    cnt=0
    while cnt<=n:
        if(cnt%2==0):
            yield cnt
        cnt+=1
a=int(input())
print(", ".join(map(str, list(fun(a)))))
    