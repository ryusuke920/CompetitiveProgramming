N, M = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
cnt = [0]*M
ans = 0
for i in range(N):
    cnt[A[i]] += 1
for i in range(M):
    if cnt[i] == 0:
        exit(print(0))
    
for i in reversed(range(N)):
    cnt[A[i]] -= 1
    ans += 1
    if cnt[A[i]] == 0:
        break
print(ans)