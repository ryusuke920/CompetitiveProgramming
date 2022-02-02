a, b = map(int,input().split())
for i in range(a, b + 1):
    if "3" in str(i) or i % 3 == 0:
        print(i)