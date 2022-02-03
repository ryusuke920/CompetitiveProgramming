#n = int(input())
a, b, c, d = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0

B = a
R = 0
ans = 0
while True:
    if B <= R * d:
        exit(print(ans))
    ans += 1
    B += b
    R += c
    if ans >= 10 ** 6:
        exit(print(-1))