def main() -> None:
    S1, S2 = input().split()
    if S1 == "sick" and S2 == "sick":
        print(1)
    elif S1 == "fine" and S2 == "sick":
        print(3)
    elif S1 == "sick" and  S2 == "fine":
        print(2)
    elif S1 == "fine" and S2 == "fine":
        print(4)


if __name__ == "__main__":
    main()