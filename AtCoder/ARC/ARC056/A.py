a,b,k,l = map(int,input().split())
print(min(k//l*b + (k%l)*a, b * (k//l + 1)))