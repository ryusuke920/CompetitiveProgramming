import math
A, B ,C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = map(int,input().split())
print(A - B)
print(C + D)
print(max(0, F - E + 1))
print((G + H + I) // 3 + 1)
j = ['a', 'aa', 'aaa', 'aaai', 'aaaji', 'aabaji', 'agabaji', 'dagabaji']
print(j[J - 1])
while K % 61 != L:
    K += 59
K += 59 * 61 * (M - 1)
num = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128] # 完全数
for i in num:
    if abs(K - i) >= N:
        ans = i
        break
print(min(K, ans))
print(max(K, ans))
print((O + P + Q) * (R + S + T) * (U + V + W) * (X + Y + Z) % 9973)