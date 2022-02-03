n = int(input())
s = list(input())

ans = [0] * n
need = []
for i, j in enumerate(s):
    if j == "1":
        ans[i] = i + 1
    else:
        need.append(i + 1)

if len(need) == 1:
    exit(print(-1))

need_cnt = 1
l = len(need)
for i in range(n):
    if ans[i] == 0:
        ans[i] = need[(need_cnt) % l]
        need_cnt += 1

print(*ans)