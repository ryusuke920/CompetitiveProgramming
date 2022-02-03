n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 10** 18
x = n
if n == 1:
    exit(print(1))
i = 1
while True:
    b = 2 ** i
    if b > n:
        break
    a = n // b
    c = n - (a * b)
    ans = min(ans, a + i + c)

    i += 1

print(ans)
