#n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
x = input()
cnt = num = 0

for i in range(3):
    if int(x[i]) == int(x[i + 1]):
        cnt += 1
    if int(x[i]) == 9:
        if int(x[i + 1]) == 0:
            num += 1
    else:
        if int(x[i + 1]) - int(x[i]) == 1:
            num += 1

if num == 3 or cnt == 3:
    print('Weak')
else:
    print('Strong')