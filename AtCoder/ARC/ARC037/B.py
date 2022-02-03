n, m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int,input().split())
    g[v - 1].append(u - 1)
    g[u - 1].append(v - 1)

#print(*g,sep = "\n")

check = [False] * n
def dfs(prev, to):
    global flag
    check[to] = True # 確認済み
    for i in g[to]:
        if i == prev: continue # 今までの頂点ならcontinue
        elif check[i]:
            flag = True
            return
        else:
            dfs(to, i)

ans = 0
for i in range(n):
    flag = False
    if check[i] == False:
        dfs(-1, i)
        if flag == False:
            ans += 1

print(ans)