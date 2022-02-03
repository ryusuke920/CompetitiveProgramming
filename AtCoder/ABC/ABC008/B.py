from collections import Counter
n = int(input())
s = [str(input()) for _ in range(n)]
ans = Counter(s)
print(ans.most_common()[0][0])