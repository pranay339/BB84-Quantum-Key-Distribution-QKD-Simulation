from modules.bit_generation import generate_bits, generate_bases
from modules.encoding import encode_bits
from modules.transmission import transmit_qubits
from modules.measurement import measure_qubits, compare_bases
from modules.error_detection import calculate_error_rate, check_security
from modules.graph import plot_error_graph
from modules.crypto_demo import encrypt_message, decrypt_message

from colorama import Fore, init
import os

init(autoreset=True)


# 📊 Dashboard
def show_dashboard(alice_key, bob_key, error_rate, n):
    print("\n📊 ===== DASHBOARD =====")

    matches = sum([1 for a, b in zip(alice_key, bob_key) if a == b])
    key_rate = len(alice_key) / n

    print(f"🔑 Key Length: {len(alice_key)}")
    print(f"✔ Matching Bits: {matches}")
    print(f"❌ Error Rate: {round(error_rate, 2)}")
    print(f"📈 Key Generation Rate: {round(key_rate, 2)}")

    if error_rate > 0.25:
        print("🚨 Status: ATTACK DETECTED")
    else:
        print("✅ Status: SECURE")


# 🚀 MAIN
n = 20

print("\n🚀 BB84 Quantum Key Distribution Simulation\n")

# 👉 Optional step view
show_steps = input("👉 Show detailed steps? (yes/no): ").lower() == "yes"

# Alice
alice_bits = generate_bits(n)
alice_bases = generate_bases(n)
qubits = encode_bits(alice_bits, alice_bases)

# Attack choice
choice = input("👉 Simulate attack? (yes/no): ")
attack = True if choice.lower() == "yes" else False

# Transmission
received_qubits = transmit_qubits(qubits, attack)

# Bob
bob_bases = generate_bases(n)
bob_bits = measure_qubits(received_qubits, bob_bases)

# 🔍 OPTIONAL STEP FLOW (CLEAN VERSION)
if show_steps:
    print("\n========== BB84 COMMUNICATION FLOW ==========")

    for i in range(n):
        print(f"\nStep {i+1}:")
        print(f"Alice Bit: {alice_bits[i]} | Alice Basis: {alice_bases[i]}")
        print(f"Encoded Qubit: {qubits[i]}")
        print(f"Transmitted Qubit: {received_qubits[i]}")
        print(f"Bob Basis: {bob_bases[i]}")
        print(f"Bob Measured Bit: {bob_bits[i]}")

        if alice_bases[i] == bob_bases[i]:
            if alice_bits[i] == bob_bits[i]:
                print(Fore.GREEN + "✔ Basis Matched & Bit Matched → Key Accepted")
            else:
                print(Fore.YELLOW + "⚠ Basis Matched but Bit Mismatch → Error")
        else:
            print(Fore.RED + "✖ Basis Mismatch → Discarded")

        print("-----------------------------------")


# Key generation
alice_key, bob_key = compare_bases(alice_bases, bob_bases, alice_bits, bob_bits)

# Error calculation
error_rate = calculate_error_rate(alice_key, bob_key)
result = check_security(error_rate)

# Output (same clean style)
print(Fore.CYAN + "\nAlice Key:", alice_key)
print(Fore.CYAN + "Bob Key:  ", bob_key)
print(Fore.YELLOW + f"\nError Rate: {round(error_rate, 2)}")

if error_rate > 0.25:
    print(Fore.RED + "🚨 " + result)
else:
    print(Fore.GREEN + "✅ " + result)

# Dashboard
show_dashboard(alice_key, bob_key, error_rate, n)

# Save results
if not os.path.exists("outputs"):
    os.makedirs("outputs")

with open("outputs/results.txt", "w", encoding="utf-8") as f:
    f.write(f"Alice Key: {alice_key}\n")
    f.write(f"Bob Key: {bob_key}\n")
    f.write(f"Error Rate: {error_rate}\n")
    f.write(f"Result: {result}\n")

print("\n💾 Results saved")

# 📊 Only ONE graph
plot_error_graph()


# 🔐 MESSAGE ENCRYPTION DEMO
choice = input("\n👉 Do you want to send a secret message? (yes/no): ")

if choice.lower() == "yes":
    print("\n🔐 ===== MESSAGE ENCRYPTION DEMO =====")

    message = input("Enter message: ")

    key_str = ''.join(map(str, alice_key))

    if len(key_str) == 0:
        print("❌ No secure key generated")
    else:
        encrypted = encrypt_message(message, key_str)
        decrypted = decrypt_message(encrypted, key_str)

        print("📨 Original Message:", message)
        print("🔒 Encrypted Message:", encrypted)
        print("🔓 Decrypted Message:", decrypted)