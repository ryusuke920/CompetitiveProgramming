from collections import Counter
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = Counter(a).most_common(k)
count = 0
for i in ans:
    count += i[1]
print(n-count)