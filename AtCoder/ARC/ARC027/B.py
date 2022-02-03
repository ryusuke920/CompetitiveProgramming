n = int(input())
x = list(input())
y = list(input())

par = [i for i in range(26)] # アルファベットの26文字
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

num = "0123456789"
cnt = [] # 定められたアルファベットかどうか
keep = [] # 単独のペアを持つかどうか
for i in range(n):
    
    if x[i] in num and y[i] in num: continue # 両方とも数字ならスキップ

    if x[i] in num: # x[i]のみが数字
        cnt.append(y[i])
    elif y[i] in num: # y[i]のみが数字
        cnt.append(x[i])
    else: # どちらもアルファベットの時 <=> 連結させる
        if x[i] == y[i]:
            if x[i] not in keep:
                keep.append(x[i])
        else:
            j = 0
            while True:
                if len(keep) >= 1:
                    if keep[j] == x[i]:
                        unite(ord(keep[j]) - 65, ord(x[i]) - 65)
                        keep.remove(x[j])

                if len(keep) >= 1:
                    if keep[j] == y[i]:
                        unite(ord(keep[j]) - 65, ord(y[i]) - 65)
                        keep.remove(y[j])
                j += 1
                if j >= len(keep) - 1:
                    break

            unite(ord(x[i]) - 65, ord(y[i]) - 65)

data = [0] * 26
for i in range(len(par)):
    data[find(i)] += 1

group = 0
ans = 0
for i in range(len(data)):
    if data[i] >= 2:
        if chr(65 + i) not in cnt:
            group += 1
        else:
            ans += 1

if group == 0:
    print(ans)
else:
    print(9 * 10 ** (group + len(keep) - 1))