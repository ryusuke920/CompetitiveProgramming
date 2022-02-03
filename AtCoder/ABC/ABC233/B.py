l, r = map(int, input().split())
s = list(input())
x = s[:l-1]
y = s[l-1:r][::-1]
z = s[r:]
print(*(x + y + z), sep='')