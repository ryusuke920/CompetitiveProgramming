x, k = list(map(str,input().split()))
k = int(k)
cnt = int(x)
if len(x) < k:
    exit(print(10 ** k))
elif len(x) == k or k == 0:
    exit(print(int(x) + 1))

x = list(x)
x = x[::-1]
for i in range(k + 1):
    x[i] = "0"
x = x[::-1]
x = list(map(int,x))
ans = 0
for i in range(len(x)):
    ans += x[-i - 1] * 10 ** i
#print(x,k,ans)
i = 0
while True:
    if ans + 10 ** i >= cnt:
        exit(print(ans + 10 ** i))
    i += 1