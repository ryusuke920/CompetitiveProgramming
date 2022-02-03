n,k = map(int,input().split())
a = list(map(int,input().split()))
used = [0]*n
now = 0
cnt = 0
roop = []
while used[now] != 2:
    if used[now] == 1:
        roop.append(a[now])
    used[now] += 1
    now = a[now] - 1
    cnt += 1
before = cnt - len(roop) * 2 # ループ前に何度移動したか
x = roop[-1]
roop = roop[:-1]
roop = roop[::-1]
roop.append(x)
roop = roop[::-1]
if before > k: # ループするより前にk回が終わってしまう場合
    used = []
    now  = cnt = 0
    while cnt < k:
        cnt += 1
        now = a[now] - 1
    exit(print(now + 1))
else:
    num = k - before
    num %= len(roop)
    print(roop[num])