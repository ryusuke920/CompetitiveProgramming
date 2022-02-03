n = int(input())
cnt = 0
st = [list(map(str,input().split())) for _ in range(n)]
x = input()
ch = 0
for i in range(n):
    if ch == 1:
        cnt += int(st[i][1])
    if st[i][0] == x:
        ch = 1
print(cnt)