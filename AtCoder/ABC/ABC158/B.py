n,a,b = map(int,input().split())
cnt = 0 #青の個数
div = n//(a+b) # a+b > 0
cnt += div*a
rest = n%(a+b) # 余り
if rest >= a:
    cnt += a
else: # rest < a: (rest == red)
    cnt += rest
print(cnt)