s = list(input())
t = input()
if len(t) > len(s): # 挿入したい文字の方が長いとアウト
    exit(print("UNRESTORABLE"))

cnt = exist = 0
for i in range(len(s) - len(t) + 1):
    ch = 1
    for j in range(len(t)):
        if s[i + j] != "?" and s[i + j] != t[j]:
            ch = 0
            break
    if ch == 1: # 挿入できる部分があればその時の場所と存在するカウンターをプラスする
        # ※挿入する位置が複数ある時は後ろの方に挿入した方が良い！！
        cnt = i
        exist = 1

if exist == 0: # どこにもTを挿入できないとアウト
    exit(print("UNRESTORABLE"))

a = 0
for i in range(len(s)):
    if i >= cnt and i <= cnt + len(t) - 1: # 範囲内だけ書き換える
        s[i] = t[a]
        a += 1
    elif s[i] == "?":
        s[i] = "a"

print(*s, sep = "")