from collections import deque
def hash(three):
    a, b, c = three[0], three[1], three[2]
    return num[a] * (52 ** 2) + num[b] * (52 ** 1) + num[c] * (52 ** 0)

n = int(input())
s = [input() for _ in range(n)]
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = {j : i for i, j in enumerate(alpha)}
cnt = 52 ** 3
rev_edges = [[] for _ in range(cnt)]
outdeg = [0] * cnt
winner = [-1] * cnt

for i in range(n):
    s1, s2 = hash(s[i][:3]), hash(s[i][-3:]) # 先頭3文字と末尾3文字
    rev_edges[s2].append(s1)
    outdeg[s1] += 1

q = deque()
for i in range(cnt):
    if outdeg[i] == 0:
        winner[i] = 0
        q.append(i)

while q:
    x = q.popleft()
    for y in rev_edges[x]:
        if winner[y] == -1:
            winner[y] = 1
            for z in rev_edges[y]:
                outdeg[z] -= 1
                if outdeg[z] == 0:
                    winner[z] = 0
                    q.append(z)

for i in range(n):
    if winner[hash(s[i][-3:])] == 1:
        print("Aoki")
    elif winner[hash(s[i][-3:])] == 0:
        print("Takahashi")
    elif winner[hash(s[i][-3:])] == -1:
        print("Draw")