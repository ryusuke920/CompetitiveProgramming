def search():
    s = input()
    
    if s > "atcoder":
        return 0
    
    for i in range(len(s)):
        if s[i] != "a": # i文字目がaならばスキップ
            if s[i] <= "t":
                return i # 先頭に持ってくる
            else:
                return i - 1 # ２文字目に持ってくる
    else:
        return -1

t = int(input())
for i in range(t):
    print(search())