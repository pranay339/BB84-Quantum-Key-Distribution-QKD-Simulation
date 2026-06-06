import random
import time

def transmit_qubits(qubits, attack=False):
    transmitted = []

    if attack:
        print("🕵️ Eve is intercepting qubits...\n")
        time.sleep(1)

    for q in qubits:
        if attack:
            transmitted.append(random.randint(0, 1))
        else:
            transmitted.append(q)

    return transmitted