n = int(input())
a, b = [0] * n, [0] * n
m = 0
for i in range(n):
    a[i], b[i] = map(int,input().split())
    m += a[i] / b[i]
l = sum(a)

#print("m=",m)
#print("l=",l)
ans = 0
m /= 2
for i in range(n):
    time = a[i] / b[i]
    if m - time < 0:
        exit(print(m * b[i] + ans))
    else:
        m -= time
        ans += a[i]
    #print(i, ans, m, time)