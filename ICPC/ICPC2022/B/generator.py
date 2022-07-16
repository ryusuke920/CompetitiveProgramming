#!/usr/bin/env python3
import random

def generate() -> None:
    n = random.randint(3, 8)
    b = [random.randint(1, 10) for _ in range(n)]
    
    print(n)
    print(*b)

generate()