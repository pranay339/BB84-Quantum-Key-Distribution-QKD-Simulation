import random

def generate_bits(n):
    choice = input("👉 1: Random Bits | 2: Manual Input: ")

    if choice == "2":
        bits = input(f"Enter {n} bits (0/1): ")
        return [int(b) for b in bits]
    else:
        return [random.randint(0, 1) for _ in range(n)]


def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]