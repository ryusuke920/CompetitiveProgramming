N,K = map(int,input().split())
NK = [list(map(int,input().split())) for _ in range(N)]
def dfs(n,k):
    if n == N:
        return k == 0
    for i in range(K):
        if dfs(n+1, k^NK[n][i]):
            return True
    return False

if dfs(0,0):
    print("Found")
else:
    print("Nothing")