'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc367/tasks/abc367_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc367/tasks/abc367_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    A, B, C = map(int, input().split())
    check = False
    if B > C:
        for i in range(B, C + 25):
            if i % 24 == A:
                check = True
    else:
        for i in range(B, C + 1):
            if i % 24 == A:
                check = True
    
    print("Yes") if check else print("No")


if __name__ == "__main__":
    main()