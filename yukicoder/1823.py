t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) <= sum(a) // 3 and sum(a) % 3 == 0:
        print('Yes')
    else:
        print('No')