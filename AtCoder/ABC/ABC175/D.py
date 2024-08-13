import sys
input = sys.stdin.readline
from collections import deque

def main() -> None:
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x) - 1, input().split()))
    C = list(map(int, input().split()))
    INF = 10**18
    cost = [[INF]*N for _ in range(N)] # cost[i][j] := i から j まで行くためのコスト
    dist = [[INF]*N for _ in range(N)]

    for i in range(N): # 始点
        now = i
        while True:
            nxt = P[now]
            if nxt == i:
                cost[i][nxt] = cost[i][now] + C[P[now]]
                dist[i][nxt] = dist[i][now] + 1
                break
            if cost[i][now] != INF:
                cost[i][nxt] = cost[i][now] + C[P[now]]
                dist[i][nxt] = dist[i][now] + 1
            else:
                cost[i][nxt] = C[P[now]]
                dist[i][nxt] = 1
            now = nxt
        
    # print(*dist,sep="\n")
    print(*cost,sep="\n")
    ans = []
    for i in range(N):
        if cost[i][i] <= 0:
            ans.append(cost[i][i])
            now = i
            cnt = 0
            while True:
                nxt = P[now]
                if nxt == i:
                    cnt += cost[i][now] + C[P[now]]
                    break
                cnt += cost[i][now] + C[P[now]]
                now = nxt
                ans.append(cnt)
        else:
            print("koko")
            num = cost[i][i] * (K // dist[i][i])
            x = K - (K // dist[i][i] * dist[i][i])
            cnt = 0
            now = i
            while True:
                if x <= 0:
                    break
                nxt = P[now]
                if nxt == i:
                    cnt += cost[i][now] + C[P[now]]
                    break
                cnt += cost[i][now] + C[P[now]]
                ans.append(num + cnt)
                now = nxt
                x -= 1
    print(max(ans))
    print(ans)



if __name__ == "__main__":
    main()