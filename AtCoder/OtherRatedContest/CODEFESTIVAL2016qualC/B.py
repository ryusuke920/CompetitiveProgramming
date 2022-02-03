k, t = map(int,input().split())
a = list(map(int,input().split()))
print(max(0, max(a) - 1 - (k - max(a))))