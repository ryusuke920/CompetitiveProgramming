n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n - 1):
    if a[i] == a[i + 1]:
        print("stay")
    elif a[i] < a[i + 1]:
        print("up", a[i + 1] - a[i])
    else:
        print("down", a[i] - a[i + 1])