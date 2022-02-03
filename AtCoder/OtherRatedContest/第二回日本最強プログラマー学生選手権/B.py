x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = cnt = 0
ans = list(set(a) ^ set(b))
ans.sort()
print(*ans)