n, m = map(int,input().split())
a = list(map(int,input().split()))

# num[i] = [x, y] := x が y 回使えるよ
num = []
for i in range(n):
    num.append([a[i], 1])

for i in range(m):
    b, c = map(int,input().split())
    num.append([c, b])

num.sort(key = lambda x: x[0], reverse = True)

ans = 0
cnt = 0 # その数をあと何回使えるか
index = 0 # 何列目を見ているか

for i in range(n):
    ans += num[0 + index][0]
    cnt += 1
    if cnt == num[0 + index][1]:
        cnt = 0
        index += 1

print(ans)