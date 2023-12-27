'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc308/tasks/abc308_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc308/tasks/abc308_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    l = [list(map(int, input().split())) + [i + 1] for i in range(n)]
    l.sort(key=lambda x: (x[0] / (x[0] + x[1]), -x[2]))

    #print(*l, sep="\n")
    ans = []
    for i in range(n):
        ans.append(l[i][2])
    print(*ans[::-1])


if __name__ == "__main__":
    main()