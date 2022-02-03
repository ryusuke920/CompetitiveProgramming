n = int(input())
a = list(map(int,input().split()))
cnt = [0]*8
free = 0
for i in range(n):
    if a[i] <= 3199:
        cnt[a[i]//400] += 1
    else:
        free += 1
print(max(1,8-cnt.count(0)),8-cnt.count(0)+free)