'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc358/tasks/abc358_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc358/tasks/abc358_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from itertools import product

def main() -> None:
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = N
    for i in product([0, 1], repeat=N):
        flag = [False]*M
        num = 0
        for j in range(N):
            if i[j]:
                num += 1
                for k in range(M):
                    if S[j][k] == "o":
                        flag[k] = True
        
        cnt = 0
        for j in range(M):
            if flag[j]:
                cnt += 1
        if cnt == M:
            ans = min(ans, num)
    
    print(ans)


if __name__ == "__main__":
    main()