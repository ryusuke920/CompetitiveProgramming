n, m, q = map(int,input().split())
problem = [0] * n
score = [[] for _ in range(n)]
for i in range(q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        ans = 0
        for i in score[s[1] - 1]:
            ans += (n - problem[i])
        print(ans)
    elif s[0] == 2:
        score[s[1] - 1].append(s[2] - 1)
        problem[s[2] - 1] += 1