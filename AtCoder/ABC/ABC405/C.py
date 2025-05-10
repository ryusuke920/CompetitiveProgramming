N = int(input())
A = list(map(int, input().split()))
sum_ = sum(A)
sum2 = 0
for i in range(N):
    sum2 += A[i]*A[i]

ans = (sum_*sum_ - sum2) // 2
print(ans)