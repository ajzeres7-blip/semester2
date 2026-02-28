n=input()
lst=list((map(int,input().split())))
count=0
for x in lst:
    if x>0:
        count+=1
print(count)