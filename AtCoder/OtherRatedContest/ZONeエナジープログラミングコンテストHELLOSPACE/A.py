#n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
s = input()
word = "ZONe"
for i in range(len(s) - 4 + 1):
    if s[i:i + 4] == word:
        ans += 1
print(ans)