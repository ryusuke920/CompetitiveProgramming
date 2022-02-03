h, w, k = map(int,input().split())

g = [list(map(lambda x:x=="x",list(input()))) for _ in [0]*h]
grid = [[0] for _ in [0] * h]

for i in range(h):
    for j in range(w):
        grid[i].append(grid[i][j] + g[i][j])

def check(x,y,k):
    for i in range(-k + 1, k):
        a = k - 1 - abs(i)
        if grid[x+i][y+a+1] != grid[x+i][y-a]:
            return False
    else:
        return True

print(sum([sum([check(x,y,k) for x in range(k-1,h-k+1)]) for y in range(k-1,w-k+1)]))