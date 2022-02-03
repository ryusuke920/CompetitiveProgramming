n = input()
ans = 0
for i in range(1, int(n) + 1):
    x = str(i)
    if '7' in x: continue # 10進数の判断
    num = ''
    x = int(i)
    while x > 0:
        num += str(x % 8)
        x //= 8
    if '7' in num: continue
    ans += 1
print(ans)