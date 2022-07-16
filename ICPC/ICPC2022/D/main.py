from itertools import product

INF = float('inf')

while True:
    n, k = map(int, input().split())
    if (n, k) == (0, 0):
        exit()
    
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    mod = 998244353

    ans = 0
    for i in product([0, 1], repeat=n - 1):
        check = 0
        for j in range(n - 1):
            if i[j] == 1:
                check += 1
        
        if check >= k:
            continue

        a = [[] for _ in range(k)]
        a[0].append(s[0])
        num = 0

        for j in range(n - 1):
            if i[j] == 1:
                num += 1

            a[num].append(s[j + 1])
    
        per = []
        while True:
            bool = True
            for i in range(k):
                if len(a[i]) != 0:
                    bool = False

            if bool:
                break
        
            mi = INF
            for i in range(k):
                if len(a[i]) >= 1:
                    mi = min(mi, a[i][0])
            
            for i in range(k):
                if len(a[i]) >= 1:
                    if a[i][0] == mi:
                        per.append(a[i].pop(0))
                        break
        
        if per == t:
            ans += 1

    print(ans)