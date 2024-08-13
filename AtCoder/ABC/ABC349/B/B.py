from collections import defaultdict

def main() -> None:
    s = input()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in s:
        d1[i] += 1
    cnt = [0]*1000
    for k, v in d1.items():
        cnt[v] += 1
    
    for i in range(1000):
        if cnt[i] != 0 and cnt[i] != 2:
            exit(print("No"))
    
    print("Yes")


if __name__ == "__main__":
    main()