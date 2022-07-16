import sys
input = sys.stdin.readline


while True:
    
    n = int(input())
    
    if n == 0:
        exit()
    
    a = list(map(int, input().split()))

    l = len(a)
    ans = 0
    for i in range(l - 2):
        if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
            ans += 1
    
    print(ans)