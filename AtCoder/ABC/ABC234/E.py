x = int(input())
ans = set()
# +のパターン
for start in range(1, 10):
    for d in range(10):
        now = str(start)
        l = 0
        while True:
            if int(now[-1]) > (int(now[-1]) + d) % 10:
                break
            now += str(int(now[-1]) + d)
            ans.add(int(now))
            l += 1
            if l >= 18:
                break

    ans.add(start)

# -のパターン
for start in range(1, 10):
    for d in range(10):
        now = str(start)
        l = 0
        while True:
            if int(now[-1]) - d < 0:
                break
            now += str(int(now[-1]) - d)

            ans.add(int(now))
            l += 1
            if l >= 20:
                break

ans = list(ans)
ans.sort()

from bisect import bisect_left
t = bisect_left(ans, x)
print(ans[t])