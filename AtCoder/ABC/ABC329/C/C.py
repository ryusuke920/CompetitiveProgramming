def RLE(S: str) -> list:
    tmp, cnt, ans = S[0], 1, []
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans.append((tmp, cnt))
            tmp = S[i]
            cnt = 1

    ans.append((tmp, cnt))

    return ans

N = int(input())
S = input()
ans = 0
from collections import defaultdict
d = defaultdict(int)
for k, v in RLE(S):
    d[k] = max(d[k], v)

for v in d.values():
    ans += v

print(ans)