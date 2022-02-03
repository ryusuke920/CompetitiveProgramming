from itertools import combinations_with_replacement as cwr
n, m, q = map(int,input().split())
a, b, c, d = [0] * q, [0] * q, [0] * q, [0] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int,input().split())

ans = 0
for i in cwr(range(1, m + 1), n): # 1 ~ m + 1 の中からm個選ぶ(問題文の単調増加を利用している)
    cnt = 0
    for j in range(q):
        if i[b[j] - 1] - i[a[j ]- 1] == c[j]:
            cnt += d[j]
    
    ans = max(ans, cnt)

print(ans)