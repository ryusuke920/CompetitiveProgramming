'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc146/tasks/arc146_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/arc146/tasks/arc146_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline


def check(k: int) -> bool:
    num = 0
    
    if 1:
        return True
    else:
       return False


def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left

def main() -> None:

    global a

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    binary_search(-1, 10 ** 18)



if __name__ == "__main__":
    main()