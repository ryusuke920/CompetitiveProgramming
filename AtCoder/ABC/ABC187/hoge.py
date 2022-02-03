n = int(input())
a = [None]*n
b = [None]*n
ab = []
for i in range(n):
    a[i], b[i] = map(int, input().split())
    ab.append([a[i], a[i] + b[i], 2 * a[i] + b[i]])
num_a = sum(a) # aoki
num_b = 0 # taka
cnt = 0
ab = sorted(ab, reverse=True, key=lambda x: x[2])

for i in range(n):
    num_a -= ab[i][0]
    num_b += ab[i][1]
    cnt += 1
    if num_a < num_b:
        print(cnt)
        exit()