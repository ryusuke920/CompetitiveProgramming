n = int(input())

num = [0] * 10 ** 7
for i in range(n):
    a, b = map(int, input().split())
    num[a] += 1
    num[b + 1] -= 1

# 累積和をとる
for i in range(len(num) - 1):
    num[i + 1] += num[i]

print(max(num))