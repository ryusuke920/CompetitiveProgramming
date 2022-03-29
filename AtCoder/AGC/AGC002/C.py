n, l = map(int, input().split())
a = list(map(int, input().split()))

num = [0] * (n - 1)
for i in range(n - 1):
    num[i] = a[i] + a[i + 1]

max_ind = num.index(max(num))
if max(num) < l:
    print('Impossible')
else:
    print('Possible')
    for i in range(n - 1):
        if max_ind == i:
            break
        print(i + 1)
    
    for i in reversed(range(n - 1)):
        print(i + 1)
        if max_ind == i:
            exit()