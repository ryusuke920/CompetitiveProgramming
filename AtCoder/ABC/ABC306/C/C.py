'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc306/tasks/abc306_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc306/tasks/abc306_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    f = [[0, 0] for _ in range(n)]
    for i in range(n):
        f[i][0] = i + 1

    for i in range(3 * n):
        cnt[a[i] - 1] += 1
        if cnt[a[i] - 1] == 2:
            f[a[i] - 1][1] = i + 1
    
    f.sort(key=lambda x: x[1])
    ans = []
    for i in range(n):
        ans.append(f[i][0])
    
    print(*ans)


if __name__ == "__main__":
    main()