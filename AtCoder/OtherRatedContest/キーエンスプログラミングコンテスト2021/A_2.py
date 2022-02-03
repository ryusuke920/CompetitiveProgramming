n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
A = a[0]
B = b[0]
print(A * B)
for i in range(n - 1):
    A = max(A, a[i + 1])
    if B < b[i + 1]:
        B = b[i + 1]
    print(A * B)