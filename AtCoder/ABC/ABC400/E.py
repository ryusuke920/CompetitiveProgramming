import sys
input = sys.stdin.readline
from math import sqrt
from bisect import bisect_left

def main() -> None:
    Q = int(input())
    N = 2*(10**6) + 10
    cnt = [0]*(N + 1)
    for i in range(2, N + 1):
        if cnt[i] != 0:
            continue
        for j in range(i, N + 1, i):
            cnt[j] += 1
    S = []
    for i in range(2, N + 1):
        if cnt[i] == 2:
            S.append(i)

    for _ in range(Q):
        A = int(input())
        a = int(sqrt(A))
        t = bisect_left(S, a)
        while True:
            if S[t]**2 <= A:
                break
            t -= 1
        print(S[t]**2)


if __name__ == "__main__":
    main()