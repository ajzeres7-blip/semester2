def down_line(a):
    i=a
    while i>=0:
        yield i
        i-=1
a=int(input())
for x in down_line(a):
    print(x,end=" ")
