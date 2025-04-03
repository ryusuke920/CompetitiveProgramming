import sys
input = sys.stdin.readline

def primes(n: int) -> list:

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    return [i for i, j in enumerate(is_prime) if j]


def main() -> None:
    from bisect import bisect_right
    N = int(input())
    p = primes(2*(10**6) + 10)
    l = len(p)
    ans = 0
    for i in p:
        if i**8 > N:
            break
        ans += 1
    print(l)
    print(p[:10])
    cnt = 0
    for i in p:
        p1 = i**2
        j = N // p1
        if j == 0:
            break
        p2 = bisect_right(p, int(j**(1/2)))
        cnt += p2
        print(p1, p2)

    print(ans + cnt, ans, cnt)


if __name__ == "__main__":
    main()