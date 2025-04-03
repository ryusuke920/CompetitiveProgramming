from itertools import product
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 10**12
for bit in product([0,1], repeat = n-1):
    cnt = 0 # 高さを更新した時の値
    h = a[0] # その地点での高さの最大値
    view = 0 # 見える数
    for i in range(n-1):
        if bit[i] == 0: # a[i+1]の高さを変更しない
            if h < a[i+1]:
                h = a[i+1]
                view += 1
                cnt += h - a[i+1]
        elif bit[i] == 1: # a[i+1]が１番高くなるように変更する
            if h < a[i+1]:
                h = a[i+1]
                cnt += h - a[i+1]
            else:
                h += 1
                cnt += h - a[i+1]
            view += 1 #絶対に見える
    if view + 1 >= k: # a[0]はいつも見えているので+1する
        ans = min(ans, cnt)
print(ans)