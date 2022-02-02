from collections import deque
while True:
    n = int(input())
    if n == 0:
        exit()
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            l = []
            for k in range(n):
                if k != i and k != j:
                    l.append(b[k])
            l.sort(reverse=True)
            if b[i] < b[j]:
                l.append(b[j])
                l.append(b[i])
            else:
                l.append(b[i])
                l.append(b[j])

            cnt = 0
            print(l)
            while True:
                if len(l) <= 2:
                    break
                while True:
                    if len(l) >= 1:
                        if l[0] == 0:
                            l.pop(0)
                        elif len(l) == 2:
                            if l[1] == 0:
                                l.pop(1)
                        elif len(l) == 3:
                            if l[1] == 0:
                                l.pop(1)
                            elif l[2] == 0:
                                l.pop(2)
                        else:
                            break
                    else:
                        break
                if len(l) <= 2:
                    break
                if l[0] >= 1 and l[1] >= 1 and l[2] >= 1:        
                    l[0] -= 1
                    l[1] -= 1
                    l[2] -= 1
                    cnt += 1
                print(l,cnt)
            ans = max(ans, cnt)
            print()
    print(ans)