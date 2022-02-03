x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)
p = p[:x]
q = q[:y]
num = p + q + r
num.sort(reverse = True)
print(sum(num[:x + y]))