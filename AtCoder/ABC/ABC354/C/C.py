'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc354/tasks/abc354_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc354/tasks/abc354_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    l = []
    for i in range(N):
        A, C = map(int, input().split())
        l.append((C, A, i))
    l.sort()
    num = -1
    ans = []
    for i in range(N):
        c, a, ind = l[i]
        if num < a:
            num = a
            ans.append(ind + 1)
        
    print(len(ans))
    ans.sort()
    print(*ans)
    

if __name__ == "__main__":
    main()