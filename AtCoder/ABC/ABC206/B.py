n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
num = 1
while True:
    if ans >= n:
        exit(print(num - 1))
    ans += num
    num += 1