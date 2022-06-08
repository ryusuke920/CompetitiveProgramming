from itertools import count

def div(k: int) -> int:
    for i in (j * j for j in count(2)):
        if i > k:
            break
        while k % i == 0:
            k //= i

    return k

n = int(input())

ans = 0
for i in range(1, n + 1):
    i = div(i)
    for j in range(1, n + 1):
        if i * j * j > n:
            break
        ans += 1

print(ans)