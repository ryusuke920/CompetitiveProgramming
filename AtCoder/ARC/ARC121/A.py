n = int(input())
xy = [[0] * 3 for _ in range(n)]
for i in range(n):
    xy[i][0], xy[i][1] = map(int,input().split())
    xy[i][2] = i

xy.sort(key = lambda x: x[0])
ans = []
ans.append( [max(abs(xy[0][0] - xy[-1][0]), abs(xy[0][1] - xy[-1][1])), abs(xy[0][2] - xy[-1][2])])
ans.append([max(abs(xy[0][0] - xy[-2][0]), abs(xy[0][1] - xy[-2][1])), abs(xy[0][2] - xy[-2][2])])
ans.append([max(abs(xy[1][0] - xy[-1][0]), abs(xy[1][1] - xy[-1][1])), abs(xy[1][2] - xy[-1][2])])
ans.append([max(abs(xy[1][0] - xy[-2][0]), abs(xy[1][1] - xy[-2][1])), abs(xy[1][2] - xy[-2][2])])
xy.sort(key = lambda x: x[1])
ans.append( [max(abs(xy[0][0] - xy[-1][0]), abs(xy[0][1] - xy[-1][1])), abs(xy[0][2] - xy[-1][2])])
ans.append([max(abs(xy[0][0] - xy[-2][0]), abs(xy[0][1] - xy[-2][1])), abs(xy[0][2] - xy[-2][2])])
ans.append([max(abs(xy[1][0] - xy[-1][0]), abs(xy[1][1] - xy[-1][1])), abs(xy[1][2] - xy[-1][2])])
ans.append([max(abs(xy[1][0] - xy[-2][0]), abs(xy[1][1] - xy[-2][1])), abs(xy[1][2] - xy[-2][2])])
ans.sort(reverse=True)
num = [True] * (n + 1)
cnt = []

for i in range(len(ans)):
    if num[ans[i][1]]:
        num[ans[i][1]] = False
        cnt.append(ans[i][0])
cnt.sort(reverse = True)
print(cnt[1])