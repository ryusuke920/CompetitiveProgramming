'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc394/tasks/abc394_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc394/tasks/abc394_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import deque

def check(a: str, b: str) -> bool:
    if a + b == "()" or a + b == "<>" or a + b == "[]":
        return True
    else:
        return False

def main() -> None:
    S = input()
    q = deque()
    N = len(S)
    for i in range(N):
        if S[i] in "([<":
            q.append(S[i])
        else:
            if not len(q):
                exit(print("No"))
            v = q.pop()
            if not check(v, S[i]):
                exit(print("No"))
    
    if len(q):
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()