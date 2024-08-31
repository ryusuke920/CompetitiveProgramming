from sortedcontainers import SortedDict
from collections import defaultdict

H, W, N = map(int, input().split())
v = []
rows = defaultdict(list)

for _ in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    v.append((x, y))
    rows[x].append(y)

for key in rows:
    rows[key].sort()

def ans_to_string(ans):
    res = ""
    for i in range(len(ans) - 1):
        now = ans[i]
        next = ans[i + 1]
        res += 'D' * (next[0] - now[0])
        res += 'R' * (next[1] - now[1])
    return res

def main() -> None:
    dp = SortedDict()
    dp[-1] = (0, (-1, -1))
    dp[10**18] = (10**18, (10**18, 10**18))
    parents = {}

    def insert_dp(ind :int, value: int, x: int, y: int):
        while True:
            num = dp.bisect_left(ind)
            if num < len(dp) and list(dp.values())[num][0] <= value:
                dp.popnumem(num)
            else:
                break
        dp[ind] = (value, (x, y))

    for i in range(H):
        if i in rows:
            for j in range(len(rows[i])):
                ind = rows[i][j]
                num = dp.bisect(ind)
                num -= 1
                value = list(dp.values())[num][0]
                parents[(i, ind)] = list(dp.values())[num][1]
                insert_dp(ind, value + 1, i, ind)

    num = dp.bisect_left(10**18)
    num -= 1
    max_value = list(dp.values())[num][0]
    print(max_value)

    ans = []
    now = list(dp.values())[num][1]
    ans.append((H - 1, W - 1))
    while now != (-1, -1):
        ans.append(now)
        now = parents[now]
    ans.append((0, 0))
    ans.reverse()

    res = ans_to_string(ans)
    print(res)


if __name__ == "__main__":
    main()