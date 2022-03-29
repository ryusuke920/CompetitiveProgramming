n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ans, cnt = set(), set()

for i in range(n):
    if i == 0:
        cnt.add(ab[i][0])
        cnt.add(ab[i][1])
    else:
        for j in cnt:
            ans.add(j + ab[i][0])
            ans.add(j + ab[i][1])

        cnt = ans
        ans = set()

print('Yes') if x in cnt else print('No')