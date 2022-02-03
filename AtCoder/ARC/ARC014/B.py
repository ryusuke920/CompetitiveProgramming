n = int(input())
t = input()
word = [t]
num = -1
for i in range(n-1):
    w = input()
    num *= -1
    if w not in word and w[0] == word[-1][-1]:
        word.append(w)
    else:
        if num == 1:
            print("WIN")
            exit()
        else:
            print("LOSE")
            exit()
print("DRAW")