# 三分探索
p = float(input())
def f(x):
    return x + p/2**(x/1.5)

ma = 1000
mi = 0
while ma - mi > 0.000000001:
    mid_left = (ma - mi)/3 + mi
    mid_right = (ma - mi)*2/3 + mi
    if f(mid_left) >= f(mid_right): # 0 ~ mid_leftには最小値が存在しない
        mi  = mid_left
    else: # mid_right ~ maには最小値が存在しない
        ma = mid_right
print(f(ma))