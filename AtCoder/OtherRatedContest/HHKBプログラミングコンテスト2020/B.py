#n = int(input())
h,w = map(int,input().split())
#a = list(map(int,input().split()))
s = [input() for i in range(h)]
cnt = 0
for i in range(h):
    for j in range(w-1):
        if s[i][j] == "." and s[i][j+1] == ".":
            cnt += 1
for i in range(w):
    for j in range(h-1):
        if s[j][i] == "." and s[j+1][i] == ".":
            cnt += 1
print(cnt)