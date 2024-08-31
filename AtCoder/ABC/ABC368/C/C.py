'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc368/tasks/abc368_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc368/tasks/abc368_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    T = 0
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N):
        # print("a", i, H[i], T)
        while True:
            if H[i] <= 0:
                break
            if T % 3 == 0:
                break
            T += 1
            if T % 3 != 0:
                H[i] -= 1
            else:
                H[i] -= 3
            # T += 1
        if H[i] <= 0:
            continue
        # print("koko", i, H[i], T)
        m = H[i] // 5
        q = H[i] % 5
        if q <= 2:
            T += q
        else:
            T += 3
        T += m*3
        # print(f"{i = }, {T = }")
    print(T)

if __name__ == "__main__":
    main()