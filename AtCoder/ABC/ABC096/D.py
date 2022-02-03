def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

n = int(input())
m = 10 ** 4
x = primes(m) # 素数の全列挙
l = len(x) # 素数の数
ans = []
for i in range(l):
    if x[i] % 5 == 1:
        ans.append(x[i])
    if len(ans) == n:
        exit(print(*ans))