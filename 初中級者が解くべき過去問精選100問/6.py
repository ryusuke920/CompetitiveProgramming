#2020/11/5
from collections import Counter
n = int(input())
s = input()
ans = 0
for i in range(1000):
    cnt = 0
    #３桁の暗証番号を設定
    i = str(i)
    if len(i) == 1:
        i = "00" + i
    elif len(i) == 2:
        i = "0" + i
    #そのようなパスワードを作成できるか判定
    for j in s:
        if i[cnt] == j:
            cnt += 1
        if cnt == 3:
            ans += 1
            break
print(ans)