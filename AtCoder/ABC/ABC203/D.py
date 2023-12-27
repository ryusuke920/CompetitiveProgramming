import sys
input = sys.stdin.readline

def binary_search(left: int, right: int) -> int:

    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        s = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if a[i][j] <= mid:
                    s[i][j + 1] = s[i][j] + 1
                else:
                    s[i][j + 1] = s[i][j]

        for j in range(n - k + 1):
            now = 0
            
            for i in range(k):
                now += s[i][j + k] - s[i][j]
            cnt = max(cnt, now)
            
            for i in range(n - k):
                now -= s[i][j + k] - s[i][j]
                now += s[i + k][j + k] - s[i + k][j]
                cnt = max(cnt, now)
        
        if cnt >= (k**2 + 1) // 2:
            right = mid
        else:
            left = mid

    return right

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

INF = 10**18
l, r = -1, INF
ans = binary_search(l, r)
print(ans)