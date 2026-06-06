def encode_bits(bits, bases):
    qubits = []

    for bit, base in zip(bits, bases):
        if base == '+':
            qubits.append(bit)
        else:
            qubits.append(1 - bit)

    return qubits