n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
if n % 100 == 0:
    print(n // 100)
else:
    print(n // 100  + 1)