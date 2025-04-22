N, M = map(int, input().split())
K, A = [], []
P = [[] for _ in range(N)]
for i in range(M):
    k, *a = map(int, input().split())
    K.append(k)
    A.append(a)
    for j in a:
        P[j - 1].append(i)
cnt = [0]*M
for i in range(M):
    cnt[i] = K[i]
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in P[B[i] - 1]:
        cnt[j] -= 1
        if cnt[j] == 0:
            ans += 1
    print(ans)