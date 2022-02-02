n = int(input())
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

x = factorization(n)
num = []
for i in range(len(x)):
    for _ in range(x[i][1]):
        num.append(x[i][0])
print(f'{n}:', *num)