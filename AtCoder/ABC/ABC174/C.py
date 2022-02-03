k = int(input())
if k%2 == 0 or k%5 == 0:
    print(-1)
    exit()

i = 0
mod = 0
while True:
    mod = (mod*10 + 7)%k
    i += 1
    if mod == 0:
        print(i)
        break