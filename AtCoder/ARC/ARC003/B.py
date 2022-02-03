n = int(input())
s = [str(input()) for _ in range(n)]
for i in range(n):
    s[i] = s[i][::-1]
s.sort()
for i in range(n):
    print(s[i][::-1])