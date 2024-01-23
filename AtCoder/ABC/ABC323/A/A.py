def main() -> None:
    S = input()
    for i in range(1, len(S), 2):
        if S[i] == "1":
            exit(print("No"))
    print("Yes")


if __name__ == "__main__":
    main()