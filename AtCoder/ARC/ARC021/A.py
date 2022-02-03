a = [list(map(int,input().split())) for _ in range(4)]
for i in range(4):
    for j in range(3):
        if a[i][j] == a[i][j+1] or a[j][i] == a[j+1][i]:
            print("CONTINUE")
            exit()
print("GAMEOVER")