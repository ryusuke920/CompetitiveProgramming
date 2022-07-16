from collections import defaultdict

s = input()

d = defaultdict(int)
d['A'] = 0
d['B'] = 1
d['C'] = 2
char = "ABC"

for _ in range(int(input())):
    t, k = map(int, input().split())
    k -= 1

    # スタートの文字を求める
    if t > 60:
        start = 0
    else:
        start = k // 2 ** t
    
    # t 区間での 2進数を求める（※s^ti[0]から計算すると TLE ）
    if start == 0:
        num = k
    else:
        num = k - start * (2 ** t)
    
    # 左の個数と右の個数を求める
    b = bin(num)[2:]
    right = 0
    for i in b:
        if i == '1':
            right += 1
    
    left = t - right

    cnt = (left + right * 2) % 3

    print(char[(d[s[start]] + cnt) % 3])