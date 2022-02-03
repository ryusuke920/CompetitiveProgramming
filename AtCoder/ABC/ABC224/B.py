h, w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

for i in range(h - 1):
    for j in range(i + 1, h):
        for k in range(w - 1):
            for l in range(k + 1, w):
                if a[i][k] + a[j][l] > a[j][k] + a[i][l]:
                    exit(print("No"))

print("Yes")