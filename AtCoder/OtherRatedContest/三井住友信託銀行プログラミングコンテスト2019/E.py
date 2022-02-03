n = int(input())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7
num = [0] * (n + 1)
num[0] = 3
ans = 1
for i in a:
    ans *= num[i]
    num[i] -= 1
    num[i + 1] += 1
    ans %= mod

print(ans)