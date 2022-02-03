x = int(input())
#5x^4 <= 10^9
#x = 150くらい？
for i in range(-150,150):
    for j in range(-151,149):
        if i**5 - j**5 == x:
            print(i,j)
            exit()