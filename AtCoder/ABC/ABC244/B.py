n = int(input())
t = input()

ans = [0, 0]
num = [[0, 1], [-1, 0], [0, -1], [1, 0]]
cnt = 0

for i in t:
    if i == 'S':
        ans[0] += num[cnt][0]
        ans[1] += num[cnt][1]
    else:
        cnt += 1
        cnt %= 4

print(ans[1], ans[0])