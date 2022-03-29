n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = set()
y = set()
for i in a:
    x.add(i)
for i in b:
    y.add(i)

cnt = 0
ans = set()
for i in range(n):
    if a[i] == b[i]:
        cnt += 1
    else:
        if a[i] in y:
            ans.add(a[i])

print(cnt, len(ans))