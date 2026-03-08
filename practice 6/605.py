S=input()
x=any(x in 'aeiouAEIOU' for x in S)
if x:
    print("Yes")
else:
    print("No")
    