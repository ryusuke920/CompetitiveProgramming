a, b, c = map(int, input().split())
k = int(input())

mod = 10 ** 9 + 7

cnt = pow(a, 2 * k, mod) * pow(b, 2 * k, mod) * pow(c, 2 * k, mod)

print(cnt % mod)