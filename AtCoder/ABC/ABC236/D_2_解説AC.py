def dfs(bool: list, cnt: int):
    """
    bool: 人 i がペアを作っているかの判定
    cnt: xor の値
    """
    global ans, n2

    # 終わるときの処理
    start = -1
    for i in range(n2):
        # print("initial bool: {0}, start: {1}, i: {2}".format(bool, start, i))
        if not bool[i]:  # まだ組み合わせていない人がいるとき
            start = i  # 最も左の人をペア作成の基準にする
            break
    if start == -1:  # 全ての人が組み合わせているとき
        ans = max(ans, cnt)
        # print(cnt)
        return

    # 続くときの1ステップ分の処理
    bool[start] = True  # 最も左の人ペアの一人にする
    for i in range(start + 1, n2):
        if not bool[i]:  # まだ組み合わせていない人がいて最左の人でないとき
            bool[i] = True  # その人もペアのもう一人にする
            # print("first bool: {0}, start: {1}, i: {2}".format(bool, start, i))
            dfs(bool, cnt ^ a[start][i])  # ペアを作って再帰
            bool[i] = False  # もとの状態に戻す！（大事）
            # print("second bool: {0}, start: {1}, i: {2}".format(bool, start, i))
    bool[start] = False  # この一行を入れないと最左の人は常にTrueになる


n = int(input())
n2 = 2*n
a = [[0] * (i + 1) + list(map(int, input().split())) for i in range(n2 - 1)]
ans = 0
bool = [False]*n2
dfs(bool, 0)
print(ans)