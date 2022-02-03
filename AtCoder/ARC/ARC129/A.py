n, l, r = map(int,input().split())
 
def f(x):
    ans = 0
    for i in range(len(int(bin(x)[2:]))):
        if 2 ** i ^ n < n:
            ans += min(2 ** (i + 1) - 1, r) - 2 ** i + 1
    return ans
 
print(f(r) - f(l - 1))