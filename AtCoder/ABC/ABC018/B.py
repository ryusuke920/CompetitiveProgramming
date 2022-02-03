s = str(input())
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    mid = s[a-1:b:1]
    mid = mid[::-1]
    s = s[:a-1] + mid + s[b:]
print(s)