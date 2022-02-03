S = input()
length = len(S)
ans = 0
print(len(S))
for i in range(length):
    ans += sum([int(S[i]) * (10**k) * 2**(max(0, length-i-k-2) + i) for k in range(length - i)])

print(ans % 998244353)
