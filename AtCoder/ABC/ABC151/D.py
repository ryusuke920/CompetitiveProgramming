from collections import deque
h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#": continue
        dis = [[-1] * w for _ in range(h)]
        dis[i][j] = 0
        que = deque()
        que.append((i, j)) # 現在地を追加
        while que: # queの中身が0になるまで続ける
            #print(que)
            i, j = que.popleft() # 1つずつみていく
            ans = max(ans, dis[i][j]) # 最大値の更新
            for k, l in (i - 1, j), (i, j + 1), (i + 1, j),(i, j - 1):
                if 0 <= k < h and 0 <= l < w and s[k][l] == "." and dis[k][l] == -1:
                    dis[k][l] = dis[i][j] + 1
                    que.append((k, l))
print(ans)