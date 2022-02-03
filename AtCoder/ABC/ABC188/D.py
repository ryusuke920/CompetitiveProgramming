import sys
input = sys.stdin.readline
n, c = map(int,input().split())
service = []
for i in range(n):
    A, B, C = map(int,input().split())
    A -= 1 # bはいもす法の関係によりそのまま
    service.append((A, B, C))

# 日付を昇順に追加する
day = set()
for i, j, k in service:
    day.add(i)
    day.add(j)
day = sorted(day) # 昇順にソート

# 座圧を行う
date = {}
for i, j in enumerate(day):
    date[j] = i
print(date)

money = [0] * len(day)
for i, j, k in service:
    money[date[i]] += k
    money[date[j]] -= k

for i in range(len(day) - 1):
    money[i + 1] += money[i]

ans = 0
for i in range(len(day) - 1):
    ans += (day[i + 1] - day[i]) * min(c, money[i])

print(ans)