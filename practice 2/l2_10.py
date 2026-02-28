n=int(input())
array=list(map(int,input().split()))
array.sort()
array.reverse()
for x in array:
    print(x, end=" ")