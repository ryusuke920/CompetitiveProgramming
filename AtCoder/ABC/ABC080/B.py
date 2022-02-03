n = int(input())
ans = 0
ch = n
while n!=0:
    ans += n%10
    n = n // 10
if ch % ans == 0:
    print("Yes")
else:
    print("No")