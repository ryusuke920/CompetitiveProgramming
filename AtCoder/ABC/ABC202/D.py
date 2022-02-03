from math import factorial as f
a, b, k = map(int,input().split())

def combination(n, k):
    return f(n) // (f(k) * f(n - k))

ans = []
n = a + b

while len(ans) < n:

    if k <= 1:
        ans.append("a" * a + "b" * b)
        break

    x = combination(a + b - 1, a - 1)

    if x >= k:
        ans.append("a")
        a -= 1
    else:
        ans.append("b")
        b -= 1
        k -= x

print("".join(ans))