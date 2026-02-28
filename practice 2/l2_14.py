n = int(input())
lst= list(map(int, input().split()))
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
mxfr = -1
result = None

for element, freq in counts.items():
    if freq > mxfr:
        mxfr = freq
        result = element
        
    elif freq == mxfr:
        if element < result:
            result= element

print(result)