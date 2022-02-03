from heapq import heappop, heappush, heapify

n = int(input())
s = input()

q = []
heapify(q)
for i in s:
    heappush(q, ord(i))

ans = [None] * n
for i in range(n):
    t = heappop(q)
    alpha = chr(t)
    if ord(alpha) < ord(s[i]):
        ans[i] = alpha
        ans[-1 - i] = s[i]
    else:
        ans[i] = s[i]
        ans[-1 - i] = alpha
print(ans)
print(''.join(ans))