a = int(input())
def keta(n):
    i = 0
    ans = 0
    num = n
    while n > 0:
        ans += num**i * (n%10)
        i += 1
        n //= 10
    return ans

for i in range(10,10001):
    if keta(i) == a:
        print(i)
        break
else:
    print(-1)