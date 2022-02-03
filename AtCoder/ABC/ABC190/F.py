import copy
n = int(input())
a = list(map(int,input().split()))

def BIT(A: list) -> int:
    "転倒数を求める"
    cnt = 0
    n = len(A)
    if n > 1:
        A1 = A[: n >> 1]
        A2 = A[n >> 1 :]
        cnt += BIT(A1)
        cnt += BIT(A2)
        i1, i2 = 0, 0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n // 2 - i1
    return cnt

x = copy.copy(a)
ans = BIT(x)
print(ans)
for i in range(n - 1):
    ans -= a[i]
    ans += n - a[i] - 1
    print(ans)