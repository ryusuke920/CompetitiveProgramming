n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from itertools import permutations
mod = 10 ** 9 + 7
for i in permutations(range(n)):
    ans = 0
    l = 1
    for j in range(n):
        num = i[j]
        ans += a[num] * l
        l *= b[num]
        ans %= mod
 #   print(ans)
    if ans == 2048669:
        print(i)