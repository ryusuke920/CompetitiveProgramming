#!/usr/bin/env python3
import random

def generate() -> None:

    k = random.randint(1, 20)
    n = random.randint(k, 20)
    print(n, k)

    s = [i + 1 for i in range(n)]
    t = [i + 1 for i in range(n)]
    random.shuffle(s)
    random.shuffle(t)
    print(*s)
    print(*t)
    

generate()