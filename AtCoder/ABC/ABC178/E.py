n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int,input().split())
# Zi = Xi + Yi, Wi = Xi - Yi
# ans = max( max(Zi) - min(Zi), max(Wi) - min(Wi) )

z = []
w = []
for i in range(n):
    z.append(x[i] + y[i])
    w.append(x[i] - y[i])
print(max(max(z) - min(z), max(w) - min(w)))