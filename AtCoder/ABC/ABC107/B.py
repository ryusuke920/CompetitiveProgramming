h,w = map(int,input().split())
ch = []
for i in range(h):
    a = str(input())
    if "#" in a:
        ch.append(a)
h = len(ch)
bit = [0]*w
for i in range(h):
    for j in range(w):
        if ch[i][j] == "#":
            bit[j] = 1

for i in range(h):
    ans = ""
    for j in range(w):
        ans += ch[i][j]*bit[j]
    print(ans)