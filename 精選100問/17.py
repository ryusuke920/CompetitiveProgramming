from itertools import permutations
k = int(input())
rc = [list(map(int,input().split())) for _ in range(k)]
for p in permutations(range(8)): # 各行の何列目にQを置くかの順列を生成
    flag = True # bool判定用
    for i,j in rc:
        if p[i] != j: # p（生成された順列）が入力値の条件を満たしてるか判定する
            flag = False
    if not flag: continue # 上記を満たしていなければさよなら

    for k in range(8):
        for l in range(8): # https://twitter.com/ryusuke__h/status/1329086907884572674
            if k == l: continue
            if abs(p[k] - p[l]) == abs(k - l):
                flag = False
    if flag:
        for i in p:
            ans = ["."]*8
            ans[i] = "Q"
            print(i,p,ans)
            print("".join(ans))