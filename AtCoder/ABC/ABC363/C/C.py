N, K = map(int, input().split())
S = list(input())

from itertools import permutations
from collections import deque
ans = set()
for i in permutations(range(N)):
    t = ""
    for j in range(N):
        t += S[i[j]]
    flag = False
    l = deque()
    for j in range(K):
        l.append(t[j])

    if l != l[::-1]:
        ans.add(t)
    for i in range(N - K):
        l.popleft()
        l.append(t[j + K + 1])
        if l != l[::-1]:
            ans.add(t)

    
print(len(ans))