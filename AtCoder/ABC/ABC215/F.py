n = int(input())
x ,y = [0] * n, [0] * n

s = []
t = []
for i in range(n):
    x[i], y[i] = map(int,input().split())
    s.append(min(x[i], y[i]))

print(max(s) - min(s))