a,b,c = map(int,input().split())
print(min(a*b,min(b*c,c*a)))
#print("{:.100f}".format(a*b*c/max(a,b,c)))