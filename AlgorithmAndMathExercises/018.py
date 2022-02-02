n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 4
for i in a:
    cnt[i // 100 - 1] += 1

ans = cnt[0] * cnt[3] + cnt[1] * cnt[2]
print(ans)