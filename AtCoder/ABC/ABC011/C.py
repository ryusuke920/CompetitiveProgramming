n = int(input())
a = [int(input()) for _ in range(3)]
cnt = 0
if n in a:
    print("NO")
    exit()
res = n%3
while n > 0:
    if n-3 not in a:
        n -= 3
        cnt += 1
    elif n-2 not in a:
        n -= 2
        cnt += 1
    elif n-1 not in a:
        n -= 1
        cnt += 1
    else:
        print("NO")
        exit()
if cnt <= 100:
    print("YES")
else:
    print("NO")