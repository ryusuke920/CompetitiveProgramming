n = int(input())
a = [int(input()) for _ in range(n)]
ans = []
up, down = 0, 0
ch = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans.append([up, down])
        up, down, ch = 0, 0, 0
    elif ch == 0: # up
        if a[i] < a[i + 1]:
            up += 1
        elif a[i] > a[i + 1]:
            ch = 1
            down += 1
        else:
            ch = 1
    elif ch == 1: # down
        if a[i] > a[i + 1]:
            down += 1
        else:
            ans.append([up, down])
            up, down, ch = 1, 0, 0
    #print(i,up,down,ans)
ans.append([up, down])
#print(ans)
num = 0
for i, j in ans:
    num  = max(num, i + j + 1)
print(num)