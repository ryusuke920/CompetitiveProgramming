def main() -> None:
    p1 = ["AD", "DA", "AC", "CA", "BD", "DB", "BE", "EB", "CE", "EC"]
    p2 = ["AE", "EA", "ED", "DE", "DC", "CD", "BC", "CB", "AB", "BA"]
    s = input()
    t = input()
    if (s in p1 and t in p1) or (s in p2 and t in p2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()