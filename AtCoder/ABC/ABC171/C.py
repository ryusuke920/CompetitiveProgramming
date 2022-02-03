n = int(input())
chrs = "abcdefghijklmnopqrstuvwxyz"
ans = ""
while n > 0:
    rest = n%26
    if rest%26 == 0:
        rest = 26
    ans += chrs[rest-1]
    n -= rest
    n //= 26
print(ans[::-1])