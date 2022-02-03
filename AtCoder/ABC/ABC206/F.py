t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    num = []
    for j in range(n):
        l, r = map(int,input().split())
        if (l - r) % 2 == 0:
            num.append(1)
        else:
            num.append(0)
    print(num.count(1), num.count(0), num)