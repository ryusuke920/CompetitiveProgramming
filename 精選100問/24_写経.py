n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
d = [0] * n # 発見時刻
f = [0] * n # 完了時刻
g = [False] * n # 訪問済みかどうか（したらTrue）

for i in range(n):
   a = list(map(int, input().split()))
   for j in range(a[1]):
       graph[a[0] - 1][a[j + 2] - 1] = 1 # 0index
print(*graph, sep = "\n")
time = 0
def search(i):
    global time
    time += 1
    d[i] = time
    g[i] = True
    for j in range(n):
        if (graph[i][j] == 1) & (g[j] == False): # 未訪問かつ行ける場所
            print(j)
            search(j)
    time += 1
    f[i] = time

for i in range(n):
    print(d)
    print(f)
    print(g)
    print()
    if not g[i]:
        search(i)
[print(i + 1, d[i], f[i]) for i in range(n)]