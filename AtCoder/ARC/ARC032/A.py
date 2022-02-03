n = int(input())
ans = n*(n+1)//2
count = 0
for i in range(1,ans+1):
    if ans%i == 0:
        count += 1
if count == 2:
    print("WANWAN")
else:
    print("BOWWOW")