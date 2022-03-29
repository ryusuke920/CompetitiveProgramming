n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = set()
cnt = set()
cnt.add(ab[0][0])
cnt.add(ab[0][1])

if n >= 2:
    for i in range(1, n):
        for j in cnt:
            ans.add(j + ab[i][0])
            ans.add(j + ab[i][1])

        cnt = ans
        if i != n - 1:
            ans = set()

    if x in ans:
        print('Yes')
    else:
        print('No')
else:
    if x in cnt:
        print('Yes')
    else:
        print('No')