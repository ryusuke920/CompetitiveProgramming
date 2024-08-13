import sys
from collections import deque
from bisect import bisect_left

INF = sys.maxsize
T = int(input().strip())

def find_first_true(arr, left, right, value):
    while left < right:
        mid = (left + right) // 2
        if arr[mid][0] == value:
            right = mid
        else:
            left = mid + 1
    return left

for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    lis = [INF] * N
    trace = [-1] * N
    dp_index = [-1] * N
    lis_length = 0
    for i in range(N):
        pos = bisect_left(lis, A[i])
        lis[pos] = A[i]
        dp_index[pos] = i
        trace[i] = dp_index[pos - 1] if pos else -1
        if pos + 1 > lis_length:
            lis_length = pos + 1

    print(lis_length)
    lis_seq = [0] * lis_length
    lis_index = dp_index[lis_length - 1]
    for i in range(lis_length - 1, -1, -1):
        lis_seq[i] = A[lis_index] + 1
        lis_index = trace[lis_index]
    
    print(" ".join(map(str, lis_seq)))