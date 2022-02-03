from collections import Counter
n = int(input())
a = list(map(int,input().split()))
q = int(input())
ans = sum(a)
count = Counter(a)
for i in range(q):
    b,c = map(int,input().split())
    ans = ans + (c-b)*count[b]
    count[c] += count[b]
    count[b] = 0
    print(ans)