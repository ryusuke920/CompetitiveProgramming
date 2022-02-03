n = int(input())
num = []
if n == 0:
    exit(print(0))
while n > 0:
    num.append(n % 36)
    n //= 36
num = num[::-1]
ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for i in num:
    ans += ch[i]
print(ans)