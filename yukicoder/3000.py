alpha = 'abcdefghijklmnopqrstuvwxyz'
password = 'cqlmdrstfxyzbanopuvweghijk'

s = input()

ans = []
for i in s:
    ans.append(password[alpha.index(i)])

print(*ans, sep='')