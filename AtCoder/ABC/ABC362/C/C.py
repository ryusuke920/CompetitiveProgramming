'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc362/tasks/abc362_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc362/tasks/abc362_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    L, R = [0]*N, [0]*N

    ans = []
    for i in range(N):
        L[i], R[i] = map(int, input().split())
        ans.append(L[i])
    
    if sum(ans) == 0:
        print("Yes")
        print(*ans)
        exit()

    if sum(ans) > 0:
        exit(print("No"))

    sum_ = sum(ans)
    for i in range(N):
        t = R[i] - L[i]
        if sum_ == 0:
            break

        if sum_ + t <= 0:
            sum_ += t
            ans[i] = R[i]
        else:
            t = abs(sum_)
            ans[i] += t
            break
    
    if sum(ans) != 0:
        exit(print("No"))
    
    print("Yes")
    # print(sum(ans))
    print(*ans)


if __name__ == "__main__":
    main()