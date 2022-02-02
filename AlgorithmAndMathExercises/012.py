n = int(input())
bool = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        bool = False
        break

print('Yes') if bool else print('No')