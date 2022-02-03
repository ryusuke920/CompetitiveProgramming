n, k = map(int,input().split())
s = input()
s = list(map(str, s.replace("01", "0,1").replace("10", "1,0").split(",")))

# 0, 1をRLE
if s[0][0] == "0":
    s = ["0"] + s
if s[-1][0] == "0":
    s = s + ["0"]

x = []
for i in range(len(s)):
    if i % 2 == 0: # 1の時
        x.append(s[i].count("1"))
    elif i % 2 == 1: # 0の時
        x.append(s[i].count("0"))

# lはindex out of range対策
l = min(len(x), 2 * k + 1)
ans = [0] * ((len(x) - l) // 2 + 1)
ans[0] = sum(x[:2 * k + 1])

# 範囲えぐい
for i in range(1, (len(x) - l) // 2 + 1):
    ans[i] = ans[i - 1] - x[2 * (i - 1)] - x[2 * (i - 1) + 1] + x[l + 2 * i - 1] + x[l + 2 * i - 2]

print(max(ans))