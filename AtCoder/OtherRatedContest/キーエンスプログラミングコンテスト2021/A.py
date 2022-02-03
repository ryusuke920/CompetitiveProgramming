n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m1 = a[0]
m2 = b[0]
ans = m1 * m2
print(m1 * m2)
t = a[0]
now = 0 # 0index
for i in range(n - 1):
    t = max(t, a[i + 1]) # 更新しないけど最大のt
    if m1 * m2 < t * b[i + 1]: # b[i]が増えたとき
        m1 = t
        m2 = b[i + 1]
    if m1 < a[i + 1]: # a[i]が増えたとき
        if a[i + 1] * b[i + 1] > m1 * m2:
            m1 = a[i + 1]
            m2 = b[i + 1] # これしかできん
    print(m1 * m2)