n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
ma = sum(a[:-1])
print(sum(a))
if ma < a[-1]:
    print(a[-1]-ma)
else:
    print(0)