n, c, k = map(int,input().split())
a = []
for i in range(n):
    t = int(input())
    a.append([t, t + k])
a.sort(key = lambda x: x[0])

ans = bus = 0
for i in range(n):
    if bus == 0:
        bus += 1
        time = a[i][1]
    elif bus >= 1:
        if time >= a[i][0] and bus <= c - 1:
            bus += 1
        else:
            ans += 1
            bus = 1
            time = a[i][1]
    if bus == c:
        ans += 1
        bus = time = 0

if bus == 0:
    print(ans)
else:
    print(ans + 1)