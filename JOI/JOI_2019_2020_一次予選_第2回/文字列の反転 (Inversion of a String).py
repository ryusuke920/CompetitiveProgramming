n,a,b = map(int,input().split())
s = input()
x = s[:a-1]
y = s[a-1:b]
y = y[::-1]
z = s[b:]
print(x+y+z)