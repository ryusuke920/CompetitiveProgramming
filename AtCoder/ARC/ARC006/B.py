n, l = map(int, input().split())
amida = [i + 1 for i in range(n)]
for i in range(l):
    line = input()
    for i in range(n - 1):
        if line[2 * i + 1] == '-':
            amida[i], amida[i + 1] = amida[i + 1], amida[i]
num = input()
print(amida[num.index('o') // 2])