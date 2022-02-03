h,w,k = map(int,input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        cnt = 0
        for l in range(h):
            for m in range(w):
                if (i >> l) & 1 == 0 and (j >> m) & 1 == 0:
                    if c[l][m] == "#":
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)