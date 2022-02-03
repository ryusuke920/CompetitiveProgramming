a, b, w = map(int,input().split())
w *= 1000 # g
cnt = 0
ma = mi = -1
for i in range(10 ** 7):
    x = a * (i + 1)
    y = b * (i + 1)
    if x <= w <= y and ma == -1:
        ma = i + 1
    if ma != -1 and x > w and mi == -1:
        mi = i

if ma == -1 or mi == -1:
    print("UNSATISFIABLE")
else:
    print(ma, mi)