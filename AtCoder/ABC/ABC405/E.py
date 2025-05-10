A, B, C, D = map(int, input().split())
mod = 998244353
max_ = max(B + D + 1, C + 1)

inv = [0]*(max_)
inv[1] = 1
for i in range(2, max_):
    inv[i] = mod - (mod // i) * inv[mod % i] % mod
# print(inv)

b = [0]*(B + 1)
b0 = 1
for i in range(1, C + 1):
    b0 = b0 * (D + i) % mod * inv[i] % mod
# print(b)
b[0] = b0
for i in range(B):
    b[i + 1] = b[i]*(i + C + D + 1) % mod * inv[i + D + 1] % mod
# print(b)
ans = 0
a_i = 1
for i in range(B + 1):
    ans = (ans + a_i*b[B - i]) % mod
    a_i = a_i*(A + i) % mod*inv[i + 1] % mod
    # print(i, ans, a_i)
print(ans)