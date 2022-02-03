n = int(input())
for i in range(1,n+1):
    ans = int(i*1.08)
    if ans == n:
        print(i)
        break
else:
    print(":(")