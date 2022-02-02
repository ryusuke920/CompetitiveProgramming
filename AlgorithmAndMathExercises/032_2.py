# bisectによる O(N log N)解法


from bisect import bisect_left

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

t = bisect_left(a, x)
if a[-1] < x:
    print('No')
elif a[t] == x:
    print('Yes')
else:
    print('No')