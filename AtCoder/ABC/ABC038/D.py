from bisect import bisect_left

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key = lambda x: (x[0], -x[1]))

ans = [a[0][1]]
for i in range(n):
    if a[i][1] > ans[-1]:
        ans.append(a[i][1])
    else:
        ans[bisect_left(ans, a[i][1])] = a[i][1]

print(len(ans))