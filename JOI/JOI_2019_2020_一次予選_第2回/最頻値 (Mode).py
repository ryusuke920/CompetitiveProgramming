from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
x = Counter(a)
print(x.most_common()[0][1])