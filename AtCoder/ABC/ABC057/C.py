n = int(input())
#桁数
def keta(x):
    count = 0
    while x != 0:
        count += 1
        x //= 10
    return count

#素数判定
ans = 1
ch = 0
for i in range(2,int(n**0.5)+1):
    if n%i == 0: #素数でない
        ans = max(ans,i)
        ch += 1
if ch == 0:
    print(keta(n))
    exit()

a = ans
b = n//a
ans = max(keta(a),keta(b))
print(min(ans, keta(n)))