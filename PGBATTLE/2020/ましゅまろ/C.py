n = int(input())
a = list(map(int,input().split()))
st = [-1]* n
num = [0]*(2*n - 1)
for i in range(2*n):
    if st[a[i]-1] == -1:
        st[a[i]-1] = i
    else:
        num[i - st[a[i]-1] - 1] += 1

ans = 0
for i in range(len(num)):
    ans += num[i]
    print(ans)