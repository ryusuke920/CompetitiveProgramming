from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

cnt = Counter(s).most_common()
print(cnt[0][0])