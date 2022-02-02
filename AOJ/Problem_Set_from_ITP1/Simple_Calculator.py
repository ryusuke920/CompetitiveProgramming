while True:
    s = input()
    if "?" in s:
        exit()
    if "/" in s:
        x = s.replace("/", "//")
        print(eval(x))
    else:
        print(eval(s))