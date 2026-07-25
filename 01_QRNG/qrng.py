""""Quantum Random Number Generator (QRNG) using Qiskit."""

from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator


def generate_random_bits(num_bits: int) -> str:
    """Generate a random bitstring of the given length using quantum superposition."""
    qc = QuantumCircuit(num_bits, num_bits)
    qc.h(range(num_bits))
    qc.measure(range(num_bits), range(num_bits))

    simulator = BasicSimulator()
    job = simulator.run(qc, shots=1)
    counts = job.result().get_counts()
    return list(counts.keys())[0]


def generate_random_int(num_bits: int) -> int:
    """Generate a random integer in [0, 2**num_bits - 1]."""
    return int(generate_random_bits(num_bits), 2)


if __name__ == "__main__":
    NUM_BITS = 8
    bits = generate_random_bits(NUM_BITS)
    print(f"Random bitstring ({NUM_BITS} bits): {bits}")
    print(f"Random integer: {int(bits, 2)}")
