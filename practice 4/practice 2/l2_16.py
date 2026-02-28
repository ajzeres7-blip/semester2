n = int(input())
lst= list(map(int, input().split()))
checked=set()
for x in lst:
    if x in checked:
        print("NO")
    else:
        print("YES")
        checked.add(x)