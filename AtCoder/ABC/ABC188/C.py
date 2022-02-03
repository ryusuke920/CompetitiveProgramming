n = int(input())
a = list(map(int,input().split()))

if n == 1:
    if a[0] < a[1]:
        exit(print(1))
    else:
        exit(print(2))

win = [[] for _ in range(n)]
for i in range(len(a)):
    win[0].append(a[i])

num = 2 ** n // 2
for i in range(n - 1):
    for j in range(num):
        if win[i][2 * j] > win[i][2 * j + 1]:
            win[i + 1].append(win[i][2 * j])
        else:
            win[i + 1].append(win[i][2 * j + 1])
    num //= 2

for i in range(len(a)):
    if a[i] == min(win[-1][0], win[-1][1]):
        exit(print(i + 1))