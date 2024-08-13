'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc361/tasks/abc361_f
oj t -c "python3 F.py"
oj s https://atcoder.jp/contests/abc361/tasks/abc361_f F.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def factorization(n: int) -> list:
    arr, tmp = [], n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    return arr

def main() -> None:
    N = int(input())
    ans = int(N**0.5)

    # print(ans)
    # i**3 以上を全探索
    for i in range(2, int(N**(1/3))):
        num = factorization(i)
        t = 3
        while True:
            a = i**t
            if a > N:
                break

            l = []
            for p, q in num:
                l.append((p, q*t))
            
            is_ok = True
            for p, q in l:
                if q % 2 == 1:
                    is_ok = False
                    break
            
            if not is_ok:
                # print(a)
                ans += 1


            t += 1
        # print(i, num)
    print(ans)
    


if __name__ == "__main__":
    main()