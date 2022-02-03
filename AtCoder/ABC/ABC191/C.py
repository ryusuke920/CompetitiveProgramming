h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]
ans = 0
d = [[0, 1], [0, 0], [1, 0], [1, 1]]
for i in range(h):
    for j in range(w):
        cnt = 0
        for k in range(4):
            if not(0 <= i + d[k][0] <= h - 1 and 0 <= j + d[k][1] <= w - 1): continue
            if s[i + d[k][0]][j + d[k][1]] == "#":
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)