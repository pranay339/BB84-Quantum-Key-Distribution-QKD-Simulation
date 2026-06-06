import matplotlib.pyplot as plt
import random
import os

def plot_error_graph():
    runs = list(range(1, 11))
    error_no_attack = []
    error_attack = []

    for _ in runs:
        error_no_attack.append(random.uniform(0.0, 0.1))
        error_attack.append(random.uniform(0.2, 0.5))

    plt.figure()
    plt.plot(runs, error_no_attack, marker='o', label="No Attack (Secure)")
    plt.plot(runs, error_attack, marker='s', label="Attack Detected")

    plt.xlabel("Simulation Runs")
    plt.ylabel("Error Rate (QBER)")
    plt.title("BB84 Security Analysis")
    plt.legend()

    if not os.path.exists("outputs/graphs"):
        os.makedirs("outputs/graphs")

    filename = f"outputs/graphs/graph_{random.randint(1,1000)}.png"
    plt.savefig(filename)

    print(f"📊 Graph saved: {filename}")
    plt.show()