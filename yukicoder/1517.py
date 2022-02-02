d = int(input())
a, b = map(int, input().split())

ans = []
for i in range(d + 1):
    ans.append(i * a + (d - i) * b)

print(min(ans))