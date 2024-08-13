from collections import deque

def check(num: int) -> bool:
    p = deque()
    for i in A:
        p.append(i)

    for i in range(K):
        min_ = p.popleft()
        max_ = p.pop()
        if len(p):
            x = max_ - p[0]
            y = p[-1] - min_
        else:
            x = max_ - min_
            y = max_ - min_
        if x < y:
            p.append(max_)
        else:
            p.appendleft(min_)

    if p[-1] - p[0] <= num:
        return True
    else:
       return False


def binary_search(left: int, right: int) -> int:
    "最小値を mid 以下にできるか"
    
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    return right

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)
K = N - K

INF = 10**18
ans = INF
for i in range(N - K + 1):
    ans = min(ans, A[i + K - 1] - A[i])

print(ans)