a = list(map(int,input().split()))
cnt = [0,0,0]
if max(a) == a[0] or min(a) == a[0]:
    cnt[0] += 1
if max(a) == a[1] or min(a) == a[1]:
    cnt[1] += 1
if max(a) == a[2] or min(a) == a[2]:
    cnt[2] += 1
for i in range(3):
    if cnt[i] == 0:
        if i == 0:
            exit(print("A"))
        elif i == 1:
            exit(print("B"))
        else:
            exit(print("C"))