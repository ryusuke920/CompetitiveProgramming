def main():
    import sys
    input = sys.stdin.readline
    
    h = [list(map(int,input().split())) for _ in range(30)] # 横のつなぎ
    v = [list(map(int,input().split())) for _ in range(29)] # 縦のつなぎ
    for i in range(1000): # クエリ
        sy, sx, ty, tx, a, e = map(float,input().split())
        sy, sx, ty, tx = int(sy), int(sx), int(ty), int(tx)
        ans = ""
        if sy <= ty and  sx <= tx:
            ans += "D" * (ty - sy)
            ans += "R" * (tx - sx)
        elif sy <= ty and sx > tx:
            ans += "D" * (ty - sy)
            ans += "L" * (sx - tx)
        elif sy > ty and sx <= tx:
            ans += "U" * (sy - ty)
            ans += "R" * (tx - sx)
        elif sy > ty and sx > tx:
            ans += "U" * (sy - ty)
            ans += "L" * (sx - tx)
        print(ans)
        sys.stdout.flush()


if __name__ == '__main__':
    main()