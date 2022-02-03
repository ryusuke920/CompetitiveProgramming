k, n, m = map(int,input().split())
a = list(map(int,input().split()))

b = [i * m / n for i in a]
sum_b = sum(int(i) for i in b)

x = m - sum_b
#print(b)
#print(sum_b)
#print(x)
c = [(-int(j) + j, i) for i, j in enumerate(b)]
c.sort(reverse=True)

b = [int(i) for i in b]

for i in range(x):
    b[c[i][1]] += 1

print(*b)