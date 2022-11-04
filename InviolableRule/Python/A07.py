d = int(input())
n = int(input())

s = [0] * (d + 100)
for _ in range(n):
    l, r = map(int, input().split())
    s[l] += 1
    s[r + 1] -= 1

for i in range(d):
    s[i + 1] += s[i]

print(*s[1 : d + 1], sep="\n")