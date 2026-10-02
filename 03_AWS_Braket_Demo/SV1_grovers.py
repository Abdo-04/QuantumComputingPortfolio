# Grover's Search Algorithm on AWS Braket
# Project 3 of 5 — Quantum Computing Portfolio


from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice
import math

def oracle(circuit, n):
    for q in range(n):
        circuit.x(q)
    circuit.cz(0, 1)
    for q in range(n):
        circuit.x(q)
    return circuit


def diffusion(circuit, n):
    for q in range(n):
        circuit.h(q)
    for q in range(n):
        circuit.x(q)
    circuit.cz(0, 1)
    for q in range(n):
        circuit.x(q)
    for q in range(n):
        circuit.h(q)
    return circuit


if __name__ == "__main__":
    print("Searching for state: |00⟩")

    n = 2
    iterations = math.floor((math.pi / 4) * math.sqrt(2 ** n))

    circuit = Circuit()
    for q in range(n):
        circuit.h(q)

    for _ in range(iterations):
        oracle(circuit, n)
        diffusion(circuit, n)

    # local run
    local_result = LocalSimulator().run(circuit, shots=1000).result()
    print("Local:", local_result.measurement_counts)

    # SV1 run
    sv1 = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
    task = sv1.run(circuit, shots=1000)
    print("Task ARN:", task.id)
    sv1_result = task.result()
    print("SV1:", sv1_result.measurement_counts)