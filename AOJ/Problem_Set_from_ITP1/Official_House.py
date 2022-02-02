n = int(input())
people = [[0]*10 for _ in range(12)]
for i in range(n):
    b,f,r,v = map(int,input().split())
    people[3*(b - 1) + f - 1][r - 1] += v
for i in range(12):
    if i == 3 or i == 6 or i == 9:
        print("#" * 20)
    print("",*people[i])