def rle(S: str) -> list:
    tmp, cnt, ans = S[0], 1, []
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans.append((tmp, cnt))
            tmp = S[i]
            cnt = 1

    ans.append((tmp, cnt))

    return ans

n, k = map(int, input().split())
s = input()

num = rle(s)
a = []
for i, j in num:
    a.append(j)

if s[0] != '1':
    a = [0] + a
if s[-1] != '1':
    a = a + [0]

# 2k + 1　の最大部分和問題
l = len(a)
ans = 0
for i in range(min(2 * k + 1, l)):
    ans += a[i]

cnt = ans
for i in range(l - 2 * k - 1):
    cnt += a[2 * k + 1 + i]
    cnt -= a[i]
    if i % 2 == 0: continue
    ans = max(ans, cnt)

print(ans)