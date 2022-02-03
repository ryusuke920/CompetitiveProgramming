a = [int(input()) for _ in range(4)]
if sum(a[:3]) <= a[3] <= sum(a[:3])+3:
    print("Yes")
else:
    print("No")