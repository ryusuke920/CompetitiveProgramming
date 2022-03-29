n = int(input())

def dfs(s: str, cnt: int):
    if len(s) == n:
        print(s)
        return
    for i in range(cnt + 1):
        dfs(s + chr(ord('a') + i), max(cnt, i + 1))

dfs('a', 1)