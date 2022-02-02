from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in combinations(range(n), 5):
    cnt = a[i[0]] + a[i[1]] + a[i[2]] + a[i[3]] + a[i[4]]
    if cnt == 1000:
        ans += 1

print(ans)