# Grover's Search Algorithm — Qiskit Implementation
# Project 2 of 5 — Quantum Computing Portfolio


from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
import math


# Define a function called oracle(qc, n) that takes the circuit and num qubits
def  oracle(qc, n):
    qc.x(range(n)) # apply X gates to qubits that should be 0 in the target state
    qc.cz(0,1)
    qc.x(range(n)) #reverse the X gates from step 1 (uncompute)

# Define a function called diffusion(qc, n) that takes the circuit and num qubits
def diffusion(qc, n):
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)  # Hadamard on last qubit
    qc.mcx(list(range(n-1)),n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))


if __name__ == "__main__":
        print("Searching for state: |00⟩")
        n = 2  # (2 qubits = search space of 4 items)
        iterations = math.floor((math.pi / 4) * math.sqrt(2 ** n))
        qc = QuantumCircuit(n, n)
        qc.h(range(n))

        for _ in range(iterations):
            oracle(qc, n)
            diffusion(qc, n)

        qc.measure(range(n), range(n))

        simulator = BasicSimulator()
        job = simulator.run(qc, shots=1000)
        counts = job.result().get_counts()
        print(counts)

        winner = max(counts, key=counts.get)
        print(f"Most measured state: {winner}")

