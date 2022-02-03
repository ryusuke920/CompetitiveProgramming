h, w, d = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

ans = [] # 答えの候補を入れておく配列
for i in range(h):
    for j in range(w):
        if d % 2 == 0 and (i + j) % 2 == 0:
            if i + j <= d:
                ans.append(a[i][j])
        elif d % 2 == 1 and (i + j) % 2 == 1:
            if i + j <= d:
                ans.append(a[i][j])

print(max(ans))