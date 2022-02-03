n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

#勝てる場合の点数
win = []
for i in range(n):
    if t[i] == "r":
        win.append("p")
    elif t[i] == "s":
        win.append("r")
    else:
        win.append("s")

#k回までの点数の和
ans = 0
for i in range(k):
    if win[i] == "r":
        ans += r
    elif win[i] == "s":
        ans += s
    else:
        ans += p

#k以降の点数（違ってるまたは０の場合は加算）
for i in range(n-k):
    if win[i] == win[i+k]:
        win[i+k] = 0
    else:
        if win[i+k] == "r" or win[i+k] == 0:
            ans += r
        elif win[i+k] == "s" or win[i+k] == 0:
            ans += s
        else:
            ans += p
print(ans)