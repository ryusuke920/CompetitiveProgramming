n = int(input())
red, blue = [], []

for _ in range(n):
    x, y = map(int,input().split())
    red.append([x, y])

for _ in range(n):
    x, y = map(int,input().split())
    blue.append([x, y])



# x 座標で貪欲する
red.sort(key = lambda x: x[0])
blue.sort(key = lambda x: x[0])
print(red)
print(blue)
num_red = 0
cnt_red, cnt_blue = 0, 0
while True:
    if cnt_red >= n - 1 and cnt_blue >= n - 1:
        break
    if red[cnt_red][0] < blue[cnt_blue][0]:
        if red[cnt_red][1] < blue[cnt_blue][1]:
            num_red += 1
            cnt_red += 1
            cnt_blue += 1
    else:
        if cnt_red <= n - 2:
            cnt_red += 1
        else:
            cnt_blue += 1
print(num_red) 

# y 座標で貪欲する
red.sort(key = lambda x: x[1])
blue.sort(key = lambda x: x[1])
