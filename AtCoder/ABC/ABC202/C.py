n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
num = [0] * n
for i in range(n):
    num[b[c[i] - 1] - 1] += 1

ans = 0
A = [0] * n
for i in range(n):
    A[a[i] - 1] += 1
#print(num)
#print(A)
for i in range(n):
    ans += A[i] * num[i]
print(ans)