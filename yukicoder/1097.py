n = int(input())
a = list(map(int, input().split()))

dob = [[0] * 10 ** 5 for _ in range(60)]

x = 0
for i in range(10 ** 5):
    r = x % n
    x += a[r]
    dob[0][i] = x

for i in range(1, 60):
    for j in range(10 ** 5):
        dob[i][j] = dob[i - 1][dob[i - 1][j]]

for _ in range(int(input())):
    k = int(input())
    now = 0
    for i in range(60):
        if k >> i & 1:
            now = dob[i][now]
    
    print(now)