n = int(input());a = list(map(int,input().split()));b = list(map(int,input().split()));c = list(map(int,input().split()));from bisect import bisect_left, bisect_right;a.sort();b.sort();c.sort();ans = 0
for i in range(n):x = bisect_left(a, b[i]);y = bisect_right(c, b[i]);ans += x * (n - y)
print(ans)