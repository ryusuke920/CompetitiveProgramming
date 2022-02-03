from collections import Counter
n = int(input())
a = list(map(int,input().split()))
cnt = Counter(a)
ans = 0
for i in cnt.items():
    if i[0] > i[1]:
        ans += i[1]
    else:
        ans += i[1] - i[0]
print(ans)