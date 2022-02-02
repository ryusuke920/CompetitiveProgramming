while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int,input().split()))
    print(max(a))