from collections import defaultdict
import sys
input = sys.stdin.readline

s = input()
t = input()
l = len(s)

judge = set()
for i in s:
    judge.add(i)

d = defaultdict(int)
dd = defaultdict(int)
alpha = "abcdefghijklmnopqrstuvwxyz"
search = s * 2

for a in alpha:
    for b in alpha:
        # a -> bに最短で何文字か
        if a not in judge: continue
        if b not in judge: continue
        flag = 0 # 初期設定
        for index, word in enumerate(search):
            if flag == 0 and word == a:
                flag = 1
                start = index
            elif flag == 1 and word == b:
                    flag = 2
                    end = index
                    break
        if flag == 2:
            print(a, b, start, end)
            if d[f"{a}{b}"] == 0:
                d[f"{a}{b}"] = end - start
                if end >= l:
                    dd[f"{a}{b}"] = 1

# -1の判定
for i in t:
    if i not in judge:
        exit(print(-1))

print(d)
print(dd)
ans = 0
for i in range(len(t) - 1):
    ans += d[f"{t[i]}{t[i + 1]}"]
    ans -= dd[f"{t[i]}{t[i + 1]}"]
    print(f"i={i}, t[i]={t[i]}, t[i + 1]={t[i + 1]}, ans={ans}")

first = s.index(t[0]) + 1
print(ans, first)
print(ans + first)