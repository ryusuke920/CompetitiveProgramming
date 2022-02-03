h,w = map(int,input().split())
ans = []
for i in range(h):
    a = input()
    if "#" in a:
        ans.append(a)
# print()
h = len(ans)
bit = [0] * w
for i in range(h):
    for j in range(w):
       if ans[i][j] == "#":
           bit[j] = 1
# print(bit)
for i in range(h):
    s = ""
    for j in range(w):
        s += ans[i][j] * bit[j]
    print(s)