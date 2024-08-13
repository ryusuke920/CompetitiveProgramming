'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc354/tasks/abc354_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc354/tasks/abc354_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    A, B, C, D = map(int, input().split())
    # p = [
    #     [2, 3, 3, 4],
    #     [1, 1, 2, 4],
    #     [0, 1, 3, 4],
    #     []
    # ]
    # sx = A
    # while sx % 4 != 0:
    #     sx += 1
    # gx = C
    # while gx % 4 != 0:
    #     gx -= 1
    # print(sx, gx)

    h = (C - A) // 4 * 4
    w = (D - B) // 4 * 4
    # print(h, w)
    ans = h * w
    p1 = A + h
    p2 = B + w

    for i in range(p2, D):
        j = (i % 4 + 4) % 4
        # j = (i % 4) % 4
        w = (C - A) // 4 * 4
        ans += w

    for i in range(p1, C):
        j = (i % 4 + 4) % 4
        # j = (i % 4) % 4
        h = (D - B) // 4 * 4
        if j < 2:
            ans += h * 3 // 2
        else:
            ans += h // 2

    # split
    # for y in range(p1, C):
    #     for x in range(p2, D):
    #         num1 = (x % 4 + 4) % 4
    #         num2 = (y % 4 + 4) % 4
    #         print(num1, num2)
    #         if (num1 + num2) % 2:
    #             ans += 1
    #         elif num1 <= 1:
    #             ans += 2


    for x in range(p1, C):
        for y in range(p2, D):
            num1 = (x % 4 + 4) % 4
            num2 = (y % 4 + 4) % 4
            if (num1 + num2) % 2:
                ans += 1
            elif num1 <= 1:
                ans += 2

    print(ans)


if __name__ == "__main__":
    main()