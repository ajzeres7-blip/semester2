n=int(input())
lst=list(map(int,input().split()))
def even(x):
    if x%2==0:
        return True
    else:
        return False
new_lst=list(filter(even,lst))
print(len(new_lst))