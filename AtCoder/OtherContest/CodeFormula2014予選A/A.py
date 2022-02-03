n = int(input())
for i in range(1,101):
    if i**3 == n:
        print("YES")
        break
else:
    print("NO")