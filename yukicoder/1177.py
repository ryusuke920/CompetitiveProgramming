p, k = map(int, input().split())

ans = 10 ** (p - 1) // p

if 10 ** (p - 1) % p >= k:
    ans += 1

print(ans % (10 ** 9 + 7))