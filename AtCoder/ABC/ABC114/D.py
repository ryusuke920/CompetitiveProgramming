x = int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1)) + 1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

num = [0] * x
for i in range(1,x + 1):
    t = factorization(i)
    for j in range(len(t)):
        num[t[j][0] - 1] += t[j][1]

print(num)
two = four = fourteen = twentyfour = seventyfour = 0
for i in range(x):
    if num[i] >= 74:
        seventyfour += 1
    if num[i] >= 24:
        twentyfour += 1
    if num[i] >= 14:
        fourteen += 1
    if num[i] >= 4:
        four += 1
    if num[i] >= 2:
        two += 1

ans = 0
# 4,4,2
ans += four * (four - 1) * (two - 2) // 2
# 24,2
ans += twentyfour * (two - 1)
# 14,4
ans += fourteen * four # 互いに素だから引かない
# 74
ans += seventyfour

print(ans)