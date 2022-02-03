n = int(input())
a = [int(input()) for _ in range(n)]
ans = sorted(a)
max1 = ans[-1]
max2 = ans[-2]
for i in a:
    if i == max1:
        print(max2)
    else:
        print(max1)