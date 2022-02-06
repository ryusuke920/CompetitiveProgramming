n = int(input())
num = [1,6,3,4,2,5] # 上、下、右、左、前、奥
ans = 1
for i in range(n):
    a = input()
    if a == "North": #[2,5,3,4,6,1]
        tmp = num[0]
        num[0] = num[4]
        num[4] = num[1]
        num[1] = num[5]
        num[5] = tmp
        ans += num[0]
    elif a == "East": #[4,3,1,6,2,5]
        tmp = num[0]
        num[0] = num[3]
        num[3] = num[1]
        num[1] = num[2]
        num[2] = tmp
        ans += num[0]
    elif a == "South": #[5,2,3,4,1,6]
        tmp = num[0]
        num[0] = num[5]
        num[5] = num[1]
        num[1] - num[4]
        num[4] = tmp
        ans += num[0]
    elif a == "West": #[3,4,6,1,2,5]
        tmp = num[0]
        num[0] = num[2]
        num[2] = num[1]
        num[1] = num[3]
        num[3] = tmp
        ans += num[0]
    elif a == "Right": #[1,6,5,2,3,4]
        tmp = num[2]
        num[2] = num[5]
        num[5] = num[3]
        num[3] = num[4]
        num[4] = tmp
        ans += num[0]
    elif a == "Left": #[1,6,2,5,4,3]
        tmp = num[2]
        num[2] = num[4]
        num[4] = num[3]
        num[3] = num[5]
        num[5] = tmp
        ans += num[0]
print(ans)