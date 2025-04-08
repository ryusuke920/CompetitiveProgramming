import sys
input = sys.stdin.readline

def binary_search(left: int, right: int, a: int) -> int:
    while right - left > 1:
        b = (left + right) // 2
        X = (2**a) * (b**2)
        if X <= N:
            left = b
        else:
            right = b

    return (left + 1) // 2


N = int(input())
ans = 0
for a in range(1, 65):
    if 2**a <= N:
        ans += binary_search(0, 10**10, a)
    else:
        break

print(ans)
