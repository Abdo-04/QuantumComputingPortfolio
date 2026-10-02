# Grover's Search Algorithm  on AWS bracket — Qiskit Implementation
# Project 3 of 5 — Quantum Computing Portfolio


from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
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

