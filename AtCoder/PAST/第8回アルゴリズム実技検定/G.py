n, k = map(int,input().split())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int,input().split())

def binary_search(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2
        cnt = 0
        for x, y, z in zip(a, b, c):
            if mid < y: continue
            cnt += min(x, (mid - y) // z + 1)
        if cnt < k:
            left = mid
        else:
            right = mid
    return right # Trueの方を返す？

INF = 10 ** 18
l, r = -1, INF
print(binary_search(l, r))