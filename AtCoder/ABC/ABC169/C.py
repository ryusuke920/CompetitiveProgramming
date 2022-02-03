a,b = map(float,input().split())
a = int(a)
b *= 100.0 + 0.0001
b = int(b)
print(a*b//100)