'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc309/tasks/abc309_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc309/tasks/abc309_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def check(k: int) -> bool:
    cnt = sum_
    for i in range(n):
        a, b = l[i]
        if a < k:
            cnt -= b
    
    if cnt <= K:
        return True
    else:
       return False

def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    return right


n, K = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
sum_ = 0
for i in range(n):
    sum_ += l[i][1]

INF = 10**18
ans = binary_search(0, INF)

print(ans)