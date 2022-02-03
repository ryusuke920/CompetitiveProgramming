p = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
from math import factorial
money = [factorial(i + 1) for i in range(10)][::-1]
#print(money)
while True:
    if cnt == p:
        exit(print(ans))
    for i in range(10):
        if money[i] + cnt <= p:
            cnt += money[i]
            break

    ans += 1