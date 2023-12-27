import sys
input = sys.stdin.readline

from collections import defaultdict

def main() -> None:
    n = int(input())
    f, s = [0] * n, [0] * n
    d = defaultdict(int)
    for i in range(n):
        f[i], s[i] = map(int, input().split())
        d[f[i]] = max(d[f[i]], s[i])
    
    num = []
    for k, v in d.items():
        num.append(v)
    num.sort()
    ans = 0
    if len(num) >= 2:
        ans = num[-1] + num[-2]

    p1 = defaultdict(int)
    p2 = defaultdict(int)
    for i in range(n):
        if p1[f[i]] == 0:
            p1[f[i]] = s[i]
        else:
            if p2[f[i]] == 0:
                p2[f[i]] = s[i]
                if p1[f[i]] < p2[f[i]]:
                    p1[f[i]], p2[f[i]] = p2[f[i]], p1[f[i]]
                ans = max(ans, p1[f[i]] + p2[f[i]] // 2)
            else:
                t = [p1[f[i]], p2[f[i]], s[i]]
                t.sort()
                ans = max(ans, t[-1] + t[-2] // 2)
                p1[f[i]], p2[f[i]] = t[-1], t[-2]
    
    print(ans)



if __name__ == "__main__":
    main()