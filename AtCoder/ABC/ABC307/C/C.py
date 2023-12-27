'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc307/tasks/abc307_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc307/tasks/abc307_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:

    ha, wa = map(int, input().split())
    a = [input() for _ in range(ha)]
    hb, wb = map(int, input().split())
    b = [input() for _ in range(hb)]
    hx, wx = map(int, input().split())
    x = [input() for _ in range(hx)]

    ans = False

    for b_start_y in range(hb):
        for b_start_x in range(wb):
            seat = [["."] * 10 for _ in range(10)]
            # 左上に A
            for i in range(ha):
                for j in range(wa):
                    seat[i][j] = a[i][j]
            # B の場所を全探索
            for i in range(hb):
                for j in range(wb):
                    by = b_start_y + i
                    bx = b_start_x + j
                    if not (0 <= by < 10 and 0 <= bx < 10):
                        continue
                    if b[i][j] == "#":
                        seat[by][bx] = "#"
            

            for i in range(10):
                for j in range(10):
                    if (i + hx - 1) > 9:
                        continue
                    if (j + wx - 1) > 9:
                        continue
                    check = True
                    for ii in range(10):
                        for jj in range(10):
                            if (i + ii > 9):
                                continue
                            if (j + jj > 9):
                                continue
                            if seat[i + ii][j + jj] != x[ii][jj]:
                                check = False
                    if check:
                        print("seat")
                        print(*seat, sep="\n")

                        ans = True

    print("Yes") if ans else print("No")



if __name__ == "__main__":
    main()