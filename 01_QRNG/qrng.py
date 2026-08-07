#Quantum Random Number Generator (QRNG) using Qiskit

from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

# forgot to define the function first
def randGen(numBits: int) ->str:

    qc = QuantumCircuit(numBits,numBits)
    qc.h(range(numBits))
    qc.measure(range(numBits), range(numBits))

    simulator = BasicSimulator()
    job = simulator.run(qc, shots = 1)
    counts = job.result().get_counts()

    return list(counts.keys())[0]
def rand_Gen(num_bits: int) -> int:
    return int(randGen(num_bits), 2)

if __name__ == "__main__":
        NUM_BITS = 8
        bits = randGen(NUM_BITS)
        print(f"Random bitstring ({NUM_BITS} bits): {bits}")
        print(f"Random integer: {rand_Gen(NUM_BITS)}")
