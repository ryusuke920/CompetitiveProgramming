x = list(input())[::-1]

num = 0
for i in x:
    num += int(i)

keta = [num]
for i in range(len(x) - 1):
    num -= int(x[i])
    keta.append(num)
keta.append(0)

ans = ''
for i in range(len(keta) - 1):
    if keta[i] >= 10:
        q, r = keta[i] // 10, keta[i] % 10
        ans += str(r)
        keta[i + 1] += q
    else:
        ans += str(keta[i])

ans += str(keta[-1])
ans = ans[::-1]
i = 0
while True:
    if ans[i] == '0':
        i += 1
    else:
        break
print(ans[i:])
'''
1225
1360
99999
111105
'''