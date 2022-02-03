h,w = map(int,input().split())
s = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if i-1 >= 0 and i+1 < h and j-1 >= 0 and j+1 < w:
                if s[i-1][j] != "#" and s[i+1][j] != "#" and s[i][j-1] != "#" and s[i][j+1] != "#":
                    print("No")
                    exit()
print("Yes")