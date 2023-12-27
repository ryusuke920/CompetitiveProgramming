import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush, heappop, heapify

def main() -> None:
    N = int(input())
    dp = defaultdict(lambda: 0)
    mod = 998244353
    dp[1] = 1
    q = [1]
    heapify(q)
    s = set()
    s.add(1)
    while q:
        v = heappop(q)
        for i in range(2, 7):
            if v * i > N:
                break
            dp[v * i] += dp[v] * pow(5, -1, mod)
            dp[v * i] %= mod
            if v * i not in s:
                s.add(v * i)
                heappush(q, v * i)
    print(dp[N])


if __name__ == "__main__":
    main()