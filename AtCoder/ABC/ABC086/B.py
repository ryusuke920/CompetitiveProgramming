a = list(input().split())
ans=int(''.join(a))
for i in range(400):
    if i*i==ans:
        print("Yes")
        break
else:
    print("No")