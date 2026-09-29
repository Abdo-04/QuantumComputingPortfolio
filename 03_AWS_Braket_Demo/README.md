# Grover's Search on AWS Braket

Project 3 of 5. The same algorithm as project 2, submitted to managed cloud
quantum infrastructure instead of running locally.

## Why this project exists

Projects 1 and 2 run on a simulator on my laptop. This one demonstrates the
workflow that actual quantum computing uses: write a circuit locally, submit
it to a managed service, get results back asynchronously.

## What changed from project 2

| Qiskit | Braket |
|---|---|
| `QuantumCircuit(2, 2)` | `Circuit()` |
| `qc.cx(0, 1)` | `.cnot(0, 1)` |
| explicit `measure()` | handled by shots |
| `BasicSimulator()` | `LocalSimulator()` or `AwsDevice(arn)` |

Braket has no multi controlled X gate. For two qubits this does not matter,
since the diffusion operator reduces to H, X, CZ, X, H.

## Setup

Requires an AWS account with Braket enabled, IAM credentials configured
locally, and a billing alarm.

```bash
pip install amazon-braket-sdk
aws configure
```

## Results

Local simulator:

SV1 managed simulator:

## Cost

| Device | Cost |
|---|---|
| LocalSimulator | Free |
| SV1 | Free tier covers 1 hr/month, then $0.075/min |
| IonQ Forte | $0.30/task plus $0.08/shot |
| Rigetti Ankaa | $0.30/task plus $0.0009/shot |

This project used SV1 only, billed at the 3 second minimum.

## Running it

```bash
python braket_grovers.py
```