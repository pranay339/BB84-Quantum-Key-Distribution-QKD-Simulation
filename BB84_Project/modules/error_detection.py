def calculate_error_rate(alice_key, bob_key):
    errors = sum([1 for a, b in zip(alice_key, bob_key) if a != b])
    return errors / len(alice_key) if len(alice_key) > 0 else 0


def check_security(error_rate):
    return "Secure Communication" if error_rate <= 0.25 else "Attack Detected"