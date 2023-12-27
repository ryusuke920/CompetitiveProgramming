'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc307/tasks/abc307_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc307/tasks/abc307_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import deque


def main() -> None:
    n = int(input())
    s = list(input())

    q1, q2 = [], []
    len_ = 0
    for i in range(n):
        q1.append(s[i])
        
        if s[i] == "(":
            q2.append(i)
            len_ += 1

        if s[i] == ")":
            if len_ >= 1:
                p = q2.pop()
                len_ -= 1
                while q1.pop() != "(":
                    continue
    
    print("".join(q1))


if __name__ == "__main__":
    main()