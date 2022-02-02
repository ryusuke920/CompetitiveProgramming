n = int(input())
a = list(map(int, input().split()))

def calc(n: int, v: int) -> int:
    '溜まった分を計算する'
    if v == 0:
        if n % 2 == 0:
            return n // 2 * (n // 2 + 1)
        elif n % 2 == 1:
            return (n + 1) // 2 * ((n + 1) // 2 + 1) - (n + 1) // 2
    elif v == 1:
        if n % 2 == 0:
            return n // 2 * (n // 2 + 1) - n // 2
        elif n % 2 == 1:
            return (n + 1) // 2 * ((n + 1) // 2 + 1) - (n + 1) // 2 - (n + 1) // 2

ans, cnt, now = 0, 0, -1 # 答え・溜まってる数・今いた場所
for i in range(n):
    if now == -1:
        if a[i] == 1:
            now = 1
            cnt = 1
    else:
        if now == 0 and a[i] == 1:
                now = 1
                cnt += 1
        elif now == 1 and a[i] == 0:
                now = 0
                cnt += 1
        else:
            ans += calc(cnt, 0)
            if a[i] == 0:
                cnt, now = 0, -1
            elif a[i] == 1:
                cnt, now = 1, 1

print(ans + calc(cnt, 1))