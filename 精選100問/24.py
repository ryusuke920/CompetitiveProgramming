n = int(input())

graph = [[0] * n for _ in range(n)] # 各ノードがどこのノードに行けるかの判定
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(a[1]):
        graph[a[0] - 1][a[j + 2] - 1] = 1

visit = [False] * n # 訪問済みかどうかの判定
go = [0] * n # 発見時刻
back = [0] * n # 完了時刻
time = 0 # その時の時刻

def dfs(i):
    global time
    time += 1
    go[i] = time
    visit[i] = True
    for j in range(n):
        if visit[j] == False and graph[i][j] == 1: # 未訪問かつ行ける所
            dfs(j)
    time += 1
    back[i] = time

for i in range(n):
    if not visit[i]:
        dfs(i)

for i in range(n):
    print(i + 1, go[i], back[i])