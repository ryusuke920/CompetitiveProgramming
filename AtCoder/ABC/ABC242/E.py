for _ in range(int(input())):

    n = int(input())
    s = input()
    l = len(s)
    mod = 998244353

    if l % 2 == 0:
        cnt = 0
        dp = [0] * (l // 2 + 1)
        
    elif l % 2 == 1:
        print('even pass')