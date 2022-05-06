from itertools import product

n, K = map(int, input().split())
s = [input() for _ in range(n)]

ans = -1
for i in product([0, 1], repeat=n):
    check = [0] * 26
    for j in range(n):
        if i[j] == 1:
            for k in s[j]:
                check[ord(k) - 97] += 1
    num = 0
    for j in range(26):
        if check[j] == K:
            num += 1
    ans = max(ans, num)

print(ans)