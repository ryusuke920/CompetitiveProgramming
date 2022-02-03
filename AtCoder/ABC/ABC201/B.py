n = int(input())
a = []
for i in range(n):
    A = list(map(str,input().split()))
    A[1] = int(A[1])
    a.append(A)

a.sort(key = lambda x: x[1], reverse = True)

print(a[1][0])