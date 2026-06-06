import random

def measure_qubits(qubits, bases):
    measured = []

    for q, base in zip(qubits, bases):
        if base == '+':
            measured.append(q)
        else:
            measured.append(random.randint(0, 1))

    return measured


def compare_bases(alice_bases, bob_bases, alice_bits, bob_bits):
    alice_key = []
    bob_key = []

    for ab, bb, abit, bbit in zip(alice_bases, bob_bases, alice_bits, bob_bits):
        if ab == bb:
            alice_key.append(abit)
            bob_key.append(bbit)

    return alice_key, bob_key