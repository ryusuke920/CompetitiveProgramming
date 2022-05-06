n = int(input())
t = list(map(int, input().split()))
a = [0]

for i in range(n):
    num = '0' * t[i]
    while True:
        num += '1'
        check = int(num[::-1], 2)
        if check > a[-1]:
            a.append(check)
            break
print(a)
print(a[-1])