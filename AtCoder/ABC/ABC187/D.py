n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

c = [[0,0,0] for _ in range(n)]
for i in range(n):
    c[i][0] = (a[i] + b[i]) + a[i] #損得の合計
    c[i][1] = a[i] + b[i] # 高橋くんが訪れた際にもらえる点数
    c[i][2] = a[i] # 青木くんが減点される点数
c.sort(key = lambda x: x[0])
c.sort(reverse = True)

taka = 0
aoki = sum(a)
for i in range(n):
    taka += c[i][1]
    aoki -= c[i][2]
    if taka > aoki:
        exit(print(i + 1))