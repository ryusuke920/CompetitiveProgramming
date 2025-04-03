H, W, D = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        for k in range(H):
            for l in range(W):
                if S[k][l] == "#":
                    continue
                cnt = 0
                for a in range(H):
                    for b in range(W):
                        if S[a][b] == "#":
                            continue
                        if abs(i - a) + abs(j - b) <= D or abs(k - a) + abs(l - b) <= D:
                            cnt += 1
                ans = max(ans, cnt)
print(ans)