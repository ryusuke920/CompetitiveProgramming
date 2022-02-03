import sys
input = sys.stdin.readline
n = int(input())
y = []
a,b,c,d,e = 0,0,0,0,0
for i in range(n):
    A = tuple(map(int,input().split()))
    a = max(a, A[0])
    b = max(b, A[1])
    c = max(c, A[2])
    d = max(d, A[3])
    e = max(e, A[4])
    y.append(A)

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        skill = [max(y[i][0], y[j][0]), max(y[i][1], y[j][1]), max(y[i][2], y[j][2]), max(y[i][3], y[j][3]), max(y[i][4], y[j][4])]
        mi = skill[0]
        if mi == skill[0]:
            ans = max(ans, min(skill[1], skill[2], skill[3], skill[4], a))
        elif mi == skill[1]:
            ans = max(ans, min(skill[0], skill[2], skill[3], skill[4], b))
        elif mi == skill[2]:
            ans = max(ans, min(skill[1], skill[0], skill[3], skill[4], c))
        elif mi == skill[3]:
            ans = max(ans, min(skill[1], skill[2], skill[0], skill[4], d))
        elif mi == skill[4]:
            ans = max(ans, min(skill[1], skill[2], skill[3], skill[0], e))
print(ans)