'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc328/tasks/abc328_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc328/tasks/abc328_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, d[i - 1] + 1):
            s = set()
            for ii in str(i):
                s.add(str(ii))
            for k in str(j):
                s.add(k)
            if len(s) == 1:
                ans += 1
    
    print(ans)
        


if __name__ == "__main__":
    main()