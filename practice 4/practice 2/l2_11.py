n, l, r=(map(int,input().split()))
array=list(map(int,input().split()))
st=l-1
nd=r
new_list=array[:st]+array[st:nd][::-1]+array[nd:]
for x in new_list:
    print(x, end=" ")
