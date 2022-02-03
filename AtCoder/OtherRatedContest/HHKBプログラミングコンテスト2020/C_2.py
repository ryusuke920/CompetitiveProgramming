n = int(input())
p = list(map(int,input().split()))
Bool = [True] * (10 ** 7)
num = 0
for i in range(n):
    Bool[p[i]] = False
    while True:
        if Bool[num]:
            break
        num += 1
    print(num)