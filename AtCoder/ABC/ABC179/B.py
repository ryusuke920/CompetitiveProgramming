n = int(input())
ans = 0
cnt = 0
ch = [[0,0]]*1000
for i in range(n):
    a,b = map(int,input().split())
    ch.append([a,b])
    if a == b:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
for i in range(len(ch)):
    if ch[i][0] != ch[i][1]:
        break
else:
    print("Yes")
    exit()
if ans >= 3:
    print("Yes")
else:
    print("No")