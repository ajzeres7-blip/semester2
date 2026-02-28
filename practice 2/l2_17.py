n = int(input())
freq = {}
for _ in range(n):
    s = input().strip()
    freq[s] = freq.get(s, 0) + 1

result = 0
for count in freq.values():
    if count == 3:
        result += 1

print(result)
