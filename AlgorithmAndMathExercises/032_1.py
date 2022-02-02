# O(N)解法

n, x = map(int, input().split())
a = list(map(int, input().split()))

if x in a:
    print('Yes')
else:
    print('No')