cnt = [0]*4
for i in range(3):
    a,b = map(int,input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1
if cnt[0] == 1 and cnt[1] == 2 and cnt[2] == 2 and cnt[3] == 1:
    print("YES")
else:
    print("NO")