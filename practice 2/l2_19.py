n = int(input())
episodes = {}
for _ in range(n):
    name, k = input().split()
    k = int(k)
    episodes[name] = episodes.get(name, 0) + k

for name in sorted(episodes):
    print(name, episodes[name])
