from collections import defaultdict

def check(p: list):
    bool = True
    for i in p:
        if not i:
            bool = False
            break
    
    return bool

while True:
    n = int(input())
    if n == 0:
        exit()
    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        p[i].sort()
    
    ans = 0
    done = [False] * n
    while True:
    
        if check(done):
            break
        
        for i in range(n):
            if len(p[i]) == 0:
                done[i] = True
                continue
            if len(p[i]) == 1:
                continue

            for j in range(len(p[i]) - 1):
                if p[i][j] == p[i][j + 1]:
                    p[i].pop(j)
                    p[i].pop(j)
                    if len(p[i]) == 0:
                        done[i] = True
                        break
                    if len(p[i]) == 1:
                        continue

        for i in range(n):
            if done[i]:
                continue

            nxt = i + 1

            while True:
                nxt %= n
                if done[nxt] == False:
                    break
                nxt += 1


            p[i].sort()
            q = p[i].pop(0)
            if len(p[i]) == 0:
                done[i] = True
            p[nxt].append(q)
            p[nxt].sort()

            ans += 1
            if len(p[nxt]) == 1:
                continue
            if len(p[nxt]) == 0:
                done[nxt] = True
            for j in range(len(p[nxt]) - 1):
                if p[nxt][j] == p[nxt][j + 1]:
                    p[nxt].pop(j)
                    p[nxt].pop(j)
                    if len(p[nxt]) == 0:
                        done[nxt] = True
                        break
                    if len(p[nxt]) == 1:
                        break
                    ans += 1

    print(ans)