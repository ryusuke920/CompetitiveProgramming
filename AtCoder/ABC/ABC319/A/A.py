def main() -> None:
    t = [
        "tourist 3858",
        "ksun48 3679",
        "Benq 3658",
        "Um_nik 3648",
        "apiad 3638",
        "Stonefeang 3630",
        "ecnerwala 3613",
        "mnbvmar 3555",
        "newbiedmy 3516",
        "semiexp 3481",
    ]

    from collections import defaultdict

    d = defaultdict(int)
    for i in t:
        p, q = i.split()
        d[p] = int(q)
    s = input()
    print(d[s])


if __name__ == "__main__":
    main()