n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 3
for i in a:
    cnt[i - 1] += 1

ans = 0
for i in cnt:
    ans += i * (i - 1) // 2

print(ans)