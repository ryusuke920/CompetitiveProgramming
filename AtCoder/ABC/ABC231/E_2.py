from random import randint

n, x = map(int,input().split())
a = list(map(int,input().split()))[::-1]

def oturi(n: int) -> int:
    oturi = n - x
    if oturi == 0:
        return 0
    cnt = 0
    money = 0
    i = 0
    while True:
        money += a[i]
        cnt += 1
        if money == oturi:
            break
        if money > oturi:
            money -= a[i]
            cnt -= 1
            i += 1

    return cnt

def main():
    cnt, money = 0, 0
    i = 0
    now = 10 ** 18
    while True:
        money += a[i]
        cnt += 1
        if money > x:
            now = min(now, oturi(money) + cnt)
            money -= a[i]
            cnt -= 1
            i += 1
        if money == x:
            break

    o = oturi(money)
    ans = cnt + o

    print(ans,cnt,o,now)

main()