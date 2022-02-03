def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n, m = map(int,input().split())
a = list(map(int,input().split()))

num = set()
for i in range(n):
    if a[i] == 1: continue
    x = factorization(a[i])
    for j in range(len(x)):
        num.add(x[j][0])

num = list(num)
#print(num)
cnt = [0] * (m + 1)
cnt[0] = 1
ans = []
for i in range(len(num)):
    for j in range(m // num[i]):
        cnt[(j + 1) * num[i]] = 1

for i in range(len(cnt)):
    if cnt[i] == 0:
        ans.append(i)

print(len(ans))
print(*ans ,sep = "\n")