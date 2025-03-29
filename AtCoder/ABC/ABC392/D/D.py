'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc392/tasks/abc392_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc392/tasks/abc392_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def main() -> None:
    N = int(input())
    K, A = [], []
    for _ in range(N):
        k, *a = map(int, input().split())
        K.append(k)
        A.append(a)
    
    d = defaultdict(int)
    for i in range(N):
        for j in A[i]:
            d[f"{i}-{j}"] += 1

    ans = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            cnt = 0
            check = [False]*(10**5 + 1)
            for k in A[i]:
                if check[k]:
                    continue
                check[k] = True
                cnt += d[f"{i}-{k}"]*d[f"{j}-{k}"]
            ans.append(cnt / (K[i]*K[j]))
    print(max(ans))


if __name__ == "__main__":
    main()