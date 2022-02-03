n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
num = {}
for i in range(n):
    if d[i] not in num:
        num[d[i]] = 1
    else:
        num[d[i]] += 1

for i in range(m):
    if t[i] not in num:
        print("NO")
        exit()
    else:
        num[t[i]] -= 1

for i in num:
    if num[i] < 0:
        print("NO")
        break
else:
    print("YES")