n = int(input())
if n%2 == 1:
    print(0)
    exit()
num = 5
i = 1
ans = 0
while num**i < n:
    ans += n//num**i//2
    i += 1
print(ans)