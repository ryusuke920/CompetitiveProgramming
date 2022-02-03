s = list(input())
k = int(input())

from collections import deque
q = deque()
ans = 0
use_k = 0
cnt = 0
for right in range(len(s)):
    q.append(s[right])
    cnt += 1
    if s[right] == ".":
        use_k += 1
    if use_k > k:
        while True:
            if use_k <= k:
                break
            v = q.popleft()
            if v == ".":
                use_k -= 1    
            cnt -= 1

    ans = max(ans, cnt)

print(ans)