n = int(input())
ans = set()
for i in range(2 * n + 1):
    if i % 2 == 0:
        for j in range(1, 2 * n + 2):
            if j not in ans:
                print(j)
                ans.add(j)
                break
    elif i % 2 == 1:
        t = int(input())
        ans.add(t)