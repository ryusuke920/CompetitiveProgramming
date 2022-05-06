n, x, y = map(int, input().split())
a = list(map(int, input().split()))

b = [i for i in a[::-1]]
ma = [0] * n
i = 0
cnt = 0
while True:
    if b[i] <= x:
        cnt += 1
        ma[i] = cnt
    elif b[i] > x:
        cnt = 0
    i += 1
    if i == n:
        break

ma = ma[::-1]
print(ma)
# ma[i] := i番目から最長で伸ばせる R の範囲
ans = 0
for l in range(n):
    