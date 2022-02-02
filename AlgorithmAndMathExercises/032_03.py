# 二分探索による O(N log N)解法

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l, r = -1, n
while r - l > 1:
    mid = (l + r) // 2
    if x >= a[mid]:
        l = mid
    else:
        r = mid

print('Yes') if a[l] == x else print('No')