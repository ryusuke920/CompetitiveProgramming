def main() -> None:
    s = input()
    len_ = len(s)
    ans = set()
    for l in range(len_):
        for r in range(l, len_):
            word = []
            for k in range(l, r + 1):
                word.append(s[k])
            ans.add("".join(word))
    
    # print(ans)

    print(len(ans))

if __name__ == "__main__":
    main()