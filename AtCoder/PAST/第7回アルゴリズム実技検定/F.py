n = int(input())
num = [0] * (2 * 10 ** 5 * 24)

for i in range(n):
    d, s, t = map(int,input().split())
    for j in range(s, t):
        num[24 * (d - 1) + j] += 1

for i in num:
    if i >= 2:
        exit(print("Yes"))

print("No")