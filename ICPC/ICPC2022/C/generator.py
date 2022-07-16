#!/usr/bin/env python3
import random

def generate() -> None:
    n = random.randint(1, 10 ** 6)
    m = random.randint(1, 10 ** 6)
    
    print(n, m)

generate()