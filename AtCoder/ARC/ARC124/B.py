n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = []
for i in range(n):
    y = []
    for j in range(n):
        y.append(a[i] ^ b[j])
    x.append(y)

cnt = set(x[0])
for i in range(n - 1):
    cnt &= set(x[i + 1])

cnt = sorted(list(cnt))
print(len(cnt))
print(*cnt,sep = "\n")