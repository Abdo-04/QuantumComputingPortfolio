# Grover's Search Algorithm

Project 2 of 5 in my quantum computing portfolio. Built with Qiskit.

## What this does

Finds a marked item in an unsorted list of N items in √N steps, compared to N/2
classically. A quadratic speedup.

| Items (N) | Classical steps | Grover's steps |
|---|---|---|
| 4 | 2 | 1 |
| 1,000,000 | 500,000 | 1,000 |
| 1,000,000,000 | 500,000,000 | 31,623 |

## How it works

1. Hadamard puts all qubits in superposition, representing every possible answer at once
2. The oracle marks the target by flipping its phase, invisible to measurement
3. The diffusion operator reflects all amplitudes about their mean, amplifying the marked state
4. Steps 2 and 3 repeat √N times
5. Measure. The target appears with near 100% probability

## Results
Searching for state: |00⟩
{'00': 1000}
Most measured state: 00

## Implementation note: iteration count

The optimal iteration count is (π/4)√N, which for N=4 gives 1.57. This must be rounded
**down**. Using `round()` gives 2, which overshoots and collapses the distribution back
to uniform:

| Iterations | Target probability |
|---|---|
| 1 | 100% |
| 2 | 25% |
| 3 | 25% |

Each iteration rotates the state vector by θ = arcsin(1/√N). The probability after k
iterations is sin²((2k+1)θ). For N=4, θ = 30°, so k=1 hits sin²(90°) = 1 exactly, while
k=2 rotates past to sin²(150°) = 0.25, identical to no amplification at all.

```python
iterations = math.floor((math.pi / 4) * math.sqrt(2 ** n))
```

## Running it

```bash
python grovers.py
```

Requires Qiskit 2.5.0.