from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = defaultdict(int)
bool = True

for i in a:
    d[i] += 1

for i in b:
    if d[i] == 0:
        bool = False
        break
    d[i] -= 1

if bool:
    print("Yes")
else:
    print("No")