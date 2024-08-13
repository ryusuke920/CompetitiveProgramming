import sys
input = sys.stdin.readline
from collections import defaultdict

def add(i: int) -> None:
    global danger
    for k, v in new_factor[i]:
        num[k] += v
        if num[k] % 3 != 0 and ((num[k] - v) % 3 == 0):
            danger += 1
        if num[k] % 3 == 0 and ((num[k] - v) % 3 != 0):
            danger -= 1


def delete(i: int) -> None:
    global danger
    for k, v in new_factor[i]:
        num[k] -= v
        if num[k] % 3 == 0 and ((num[k] + v) % 3 != 0):
            danger -= 1
        if num[k] % 3 != 0 and ((num[k] + v) % 3 == 0):
            danger += 1


def Eratosthenes() -> None:
    n = max(A)
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False


    for i in range(2, n + 1):
        if primes[i]:
            min_fac[i] = i
            for j in range(2 * i, n + 1, i):
                primes[j] = False
                if min_fac[j] == -1:
                    min_fac[j] = i


def Factorization() -> None:
    for i in range(N):
        now = A[i]
        while True:
            if now == 1:
                break
            if min_fac[now] == now:
                factor[i].append(now)
                break
            else:
                factor[i].append(min_fac[now])
                now //= min_fac[now]


def main() -> None:
    global N, Q, A, min_fac, factor, num, danger, new_factor
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    block = int(N / Q ** 0.5) + 1
    queries = [[] for _ in range(int(Q**0.5) + 1)]

    for i in range(Q):
        L, R = map(lambda x: int(x) - 1, input().split())
        queries[L // block].append((i, L, R))
    
    min_fac = [-1] * (max(A) + 1) # min_fac[i] := i の最小の素因数
    factor = [[] for _ in range(N)] # factor[i] := A[i] の素因数分解
    # S[i][r] - S[i][l - 1] := [l, r] の i の素因数の個数

    Eratosthenes()
    Factorization()

    # print(min_fac[:30])
    # print(*factor[:30], sep="\n")
    new_factor = [[] for _ in range(N)]
    for i in range(N):
        d = defaultdict(int)
        for j in factor[i]:
            d[j] += 1
        for k, v in d.items():
            new_factor[i].append((k, v))
    
    # print(*new_factor, sep="\n")


    ans = [0] * Q
    left, right = 0, 0
    num = [0] * (max(A) + 1) # num[i] := [l, r] の中にある素因数 i の合計
    danger = 0 # danger >= 1 := 3 の倍数個でない素因数が存在する

    for ind, query in enumerate(queries):
        for i, l, r in sorted(query, reverse=ind%2, key=lambda x: x[2]): 
            while right <= r:
                add(right)
                right += 1
            while l < left:
                left -= 1
                add(left)
            while r + 1 < right:
                right -= 1
                delete(right)
            while left < l:
                delete(left)
                left += 1

            ans[i] = (danger == 0)

    for i in range(Q):
        print("Yes") if ans[i] else print("No")



if __name__ == "__main__":
    main()