def binary_search(N, M, A):
    low, high = 0, max(A) + 1

    while low < high:
        mid = (low + high) // 2
        total = sum(min(mid, a) for a in A)
        
        if total <= M:
            low = mid + 1
        else:
            high = mid
    
    if low > max(A):
        return "infinite"
    else:
        return low - 1


N, M = map(int, input().split())
A = list(map(int, input().split()))

print(binary_search(N, M, A))