import sys
input = sys.stdin.readline

def nCk(n: int, k: int) -> int:
    if n < 0 or k < 0 or n - k < 0:
        return 0
    
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i
    cntcnt = 1
    for i in range(1, k + 1):
        cntcnt *= i
    cntcntcnt = 1
    for i in range(1, n - k + 1):
        cntcntcnt *= i

    return cnt // (cntcnt * cntcntcnt)


def main() -> None:
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    print(sum(v[:a]) / a)
    if v[0] == v[a - 1]:
        ans = 0
        for i in range(a, b + 1):
            ans += nCk(v.count(v[0]), i)
        
        print(ans)
    else:
        cnt = 0
        for i in range(a):
            if v[i] == v[a - 1]:
                cnt += 1
        
        ans = nCk(v.count(v[a - 1]), cnt)
        print(ans)


if __name__ == "__main__":
    main()