n = int(input())
ans = ""
for i in range(1,n+1):
    if i%3 == 0:
        ans += " " + str(i)
    else:
        x = i
        while(x):
            if (x%10 == 3):
                ans += " " + str(i)
                break
            x //= 10
print(ans)