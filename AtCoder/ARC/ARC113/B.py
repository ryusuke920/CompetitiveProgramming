a,b,c = map(int,input().split())
num = a
cnt = []
while True:
    if num % 10 in cnt:
        break
    cnt.append(num % 10)
    num *= a
    num % 10

b = pow(b, c, len(cnt))
print(cnt[b - 1])