S = input()
T = input()
for i in range(len(S)):
    if S[i]!=T[i]:
        print("No")
        break
else:
    print("Yes")