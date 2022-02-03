s = str(input())
a = list(map(int,input().split()))
for i in range(4):
    s = s[:a[i]+i] + '"' + s[a[i]+i:]
print(s)