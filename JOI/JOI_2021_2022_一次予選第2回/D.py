from collections import Counter

input()
cnt = Counter(list(map(int, input().split()))).most_common()

ans = []
mi = 10 ** 18
for i, j in cnt:
    mi = min(mi, j)

for i, j in cnt:
    if j == mi:
        ans.append(i)

print(min(ans))