from itertools import product
# 10進数 -> 2進数への変換
def DeciamlToBinary(num):
    binary_number = ""
    while num > 0:
        binary_number += str(num % 2)
        num //= 2
    return binary_number

n = int(input())
a = list(map(int,input().split()))
ans = 0
lennum = 0
num = []
for j in range(n):
    num.append(DeciamlToBinary(a[j]))
    lennum = max(lennum, len(DeciamlToBinary(a[j])))
for i in range(n):
        num[i] = "0" * (lennum - len(num[i])) + num[i]
cnt = [0]* lennum
for i in range(len(num)):
    for j in range(lennum):
        cnt[j] += int(num[i][j])
for i in range(len(cnt)):
    if cnt[i] == 1:
        ans += 2 ** i
print(ans)