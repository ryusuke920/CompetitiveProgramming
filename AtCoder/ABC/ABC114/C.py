n = int(input())
def dfs(num, ch, cnt):
    if num > n:
        return
    if ch == 0b111:
        cnt.append(1)
    dfs(num*10 + 7, ch | 0b100, cnt)
    dfs(num*10 + 5, ch | 0b010, cnt)
    dfs(num*10 + 3, ch | 0b001, cnt)

arr = []
x = dfs(0,0,arr)
print(sum(arr))