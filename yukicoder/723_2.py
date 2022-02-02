from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

print(sum(bisect_right(a, x - i) - bisect_left(a, x - i) for i in a))