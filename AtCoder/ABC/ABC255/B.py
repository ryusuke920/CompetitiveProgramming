def min_int(a: int, b: int) -> int:
    "2数の最小値"
    return a if a <= b else b


def max_int(a: int, b: int) -> int:
    "2数の最大値"
    return a if a >= b else b


def min_list(a: list) -> int:
    "リストの最小値"
    global INF
    cnt = INF
    for i in range(len(a)):
        if a[i] < cnt:
            cnt = a[i]

    return cnt


def max_list(a: list) -> int:
    "リストの最大値"
    global INF
    cnt = -INF
    for i in range(len(a)):
        if a[i] > cnt:
            cnt = a[i]

    return cnt


def OutOfRange(h: int, w: int, vy: int, vx: int) -> bool:
    "BFSなどの配列外参照"
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h):
            return False
        else:
            return True


def main() -> None:
    INF = 10 ** 18
    mod = 10 ** 9 + 7
    #mod = 998244353

    #n = int(input())
    #s = input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = set()
    for i in a:
        b.add(i - 1)
    
    xy = [list(map(int, input().split())) for _ in range(n)]
    #s=[list(input()) for _ in range(h)]
    dist = [INF] * n
    for i in a:
        dist[i - 1] = 0

    for i in range(n): # 明かりを持っている人

        if i not in b:
            continue

        for j in range(n):
            if i == j:
                continue

            xi, yi = xy[i]
            xj, yj = xy[j]
            d = (xi - xj) ** 2 + (yi - yj) ** 2
            
            dist[j] = min(dist[j], d ** 0.5)
        #print('afaeff',i, dist)

    ans = 0
    #print(b)
    #print(dist)
    for i in dist:
        if i == 0:
            continue
        ans = max(ans, i)
    print(ans)





    


if __name__ == '__main__':
    main()