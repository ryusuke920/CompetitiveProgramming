N = int(input())

INF = 10**18
dp1 = [INF]*(N + 1) # 式の最短長
ans  = [""]*(N + 1)
dp_now = [INF]*(N + 1) # 項の最短長
s_term  = [""]*(N + 1)
dp_fac = [INF]*(N + 1) # 因数の最短長
s_fac  = [""]*(N + 1)

num = 0
k = 0
while True:
    k += 1
    num = num*10 + 1
    if num > N:
        break
    dp_fac[num] = k
    s_fac[num] = "1"*k

for v in range(1, N + 1):
    dp_now[v] = dp_fac[v]
    s_term[v] = s_fac[v]
    # print(dp_now)
    # print(s_term)
    # v = a*b
    a = 1
    while a * a <= v:
        if v % a == 0:
            b = v // a
            # a*b
            if dp_now[a] < INF and dp_fac[b] < INF:
                cand = dp_now[a] + 1 + dp_fac[b]
                if cand < dp_now[v]:
                    dp_now[v] = cand
                    s_term[v] = s_term[a] + "*" + s_fac[b]
            # b*a
            if dp_now[b] < INF and dp_fac[a] < INF:
                cand = dp_now[b] + 1 + dp_fac[a]
                if cand < dp_now[v]:
                    dp_now[v] = cand
                    s_term[v] = s_term[b] + "*" + s_fac[a]
        a += 1

    dp1[v] = dp_now[v]
    ans[v] = s_term[v]
    # print(dp1)
    # print(ans)

    # v = x + y, y = v - x
    for x in range(1, v):
        y = v - x
        if dp1[x] < INF and dp_now[y] < INF:
            cand = dp1[x] + 1 + dp_now[y]
            if cand < dp1[v]:
                dp1[v] = cand
                ans[v] = ans[x] + "+" + s_term[y]
    
    # ()
    len_ = dp1[v] + 2
    if len_ < dp_fac[v]:
        dp_fac[v] = len_
        s_fac[v] = "(" + ans[v] + ")"
        # print(s_fac[v])
    

    # 項、式の min
    # print(dp_fac[v], dp_now[v], dp1[v])
    if dp_fac[v] < dp_now[v]:
        dp_now[v] = dp_fac[v]
        s_term[v] = s_fac[v]


print(ans[N])
# print(*ans[:10])