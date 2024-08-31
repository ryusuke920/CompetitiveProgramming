from collections import defaultdict, deque

def solve(N, M, X1, trains):
    adj = defaultdict(list)
    in_degree = [0] * M
    delays = [float('inf')] * M
    
    # 隣接リストと入次数を構築
    for i in range(M):
        Ai, Bi, Si, Ti = trains[i]
        for j in range(M):
            Aj, Bj, Sj, Tj = trains[j]
            if Bi == Aj and Ti <= Sj:
                adj[i].append(j)
                in_degree[j] += 1
    
    # 最初の電車の遅延時間を設定
    delays[0] = X1
    
    # トポロジカルソートのためのキュー
    queue = deque()
    
    # 入次数が0のノードをキューに追加
    for i in range(M):
        if in_degree[i] == 0:
            queue.append(i)
    
    # トポロジカルソートしながら遅延時間を計算
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            delays[v] = min(delays[v], delays[u] + (Ti - Sj))
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # 結果を出力
    print(" ".join(map(str, delays[1:])))
    
# 入力処理
N, M, X1 = map(int, input().split())
trains = [tuple(map(int, input().split())) for _ in range(M)]

solve(N, M, X1, trains)
