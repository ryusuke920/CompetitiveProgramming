x = int(input())
for i in range(1,x+1):
    if 100*i <= x and x <= 105*i:
        print(1)
        break
else:
    print(0)