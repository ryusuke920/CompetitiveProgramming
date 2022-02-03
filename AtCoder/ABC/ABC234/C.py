k = int(input())
'''
2
20 22
200 202 220 222
2000 2002 2020 2022 2200 2202 2220 2222
2 ^ n個

'''
x = bin(k)[2:]

ans = ''
for i in x:
    if i == '0':
        ans += '0'
    else:
        ans += '2'

print(ans)