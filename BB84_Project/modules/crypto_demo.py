def encrypt_message(message, key):
    encrypted = ""

    for i in range(len(message)):
        # XOR each character with key digit
        encrypted += chr(ord(message[i]) ^ int(key[i % len(key)]))

    return encrypted


def decrypt_message(encrypted, key):
    decrypted = ""

    for i in range(len(encrypted)):
        # Same XOR to get original back
        decrypted += chr(ord(encrypted[i]) ^ int(key[i % len(key)]))

    return decrypted