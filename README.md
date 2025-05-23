# Quantum Circuit Simulator (NumPy-Based)

## Table of Contents

- [Overview](#overview)
- [Goals](#goals)
- [Project Structure](#project-structure)
- [Key Concepts](#key-concepts)
- [How to Run](#how-to-run)
- [What I Learned](#what-i-learned)
- [Next Steps](#next-steps)
- [References](#references)
- [License](#license)
- [Contact](#contact)

## Overview

A lightweight, extensible quantum circuit simulator built entirely using NumPy. This simulator models multi-qubit statevectors and supports core gate operations, enabling users to prototype and run simple quantum algorithms from scratch without the use of external libraries such as Qiskit.

## Features

- **Statevector-based simulation** of arbitrary quantum states
- **Gate operations:** Supports standard gates including X, Z, H, and CNOT
- **Multi-qubit support** via tensor product composition
- **Custom state initialization**
- **Measurement collapse** for partial measurements
- **Quantum teleportation** demo implemented as a correctness test
- _Planned:_ Custom gate implementation using the 'Gate' class

## Goals

- **Deepen understanding of quantum mechanics** through simulation-based exploration
- **Reinforce linear algebra concepts** like unitary transformations and tensor products
- Build **intuition** around **quantum algorithms** by implementing them from scratch
- Develop a **clean, modular simulator** that mimics the behavior of quantum state evolution
- Design **reusable tools** to support rapid prototyping of quantum protocols and algorithms
- Ensure **accuracy** and **expandability** through well-structured code and careful documentation

---

## Project Structure

- [assets/](.\assets)
  - [protocol-diagram.png](.\assets\protocol-diagram.png)
- [notebooks/](.\notebooks)
  - [prototype.ipynb](.\notebooks\prototype.ipynb)
- [src/](.\src)
  - [demos/](.\src\demos)
    - [teleportation.py](.\src\demos\teleportation.py)
  - [main.py](.\src\main.py)
  - [utils.py](.\src\utils.py)
- [.gitignore](..gitignore)
- [LICENSE](.\LICENSE)
- [README.md](.\README.md)
- [requirements.txt](.\requirements.txt)

---

## Key Concepts

- **Qubits** as complex state vectors
- **Entanglement** via the Hadamard and CNOT gates (resulting in a bell state)
- **Quantum measurement** and **state collapse**
- **Custom implementation** of state evolution (no Qiskit involved)

---

## How It Works

The `QuantumState` class contains built-in gates that can be applied to specific qubits within the state. Partial measurements automatically update the state.

### Example Usage

```python
from utils import QuantumState

# Initialize individual qubits as NumPy arrays
A = np.array([1, 0])
B = np.array([1, 0])

# Initialize two-qubit quantum state
psi = QuantumState.from_qubits(A, B)

# Apply a Hadamard to qubit 0
psi.H(0)

# Apply a CNOT with control=0 and target=1
psi.CNOT(0, 1)

# Output final state
print(psi)
```

## Demos

The [demos](./src/demos) test the correctness of the simulator by simulating quantum protocols.

### Quantum Teleportation

The [teleportation demo](.demos/teleportation.py) simulates a 3-qubit system that transmits the state of one qubit to another using entanglement and classical communication.

![image](./assets/teleportation-protocol-diagram.png)

Running the demo:

```bash
python demos/teleportation.py
```

### Deutsch's Algorithm

The [Deutsch's Algorithm demo](.demos/deutschs_algorithm.py) simulates a 2-qubit system that queries once to determine whether an unknown function $f:\Sigma\rightarrow\Sigma$ is constant (return 0) or balanced (return 1).

```bash
python demos/deutschs_algorithm.py
```

## What I Learned

While building this, I deepened my understanding of quantum state manipulation, gate operations, and how measurement impacts entangled systems. This project helped me gain confidence in applying quantum concepts using Python, and it is my first major step into the world of quantum computing.

## Next Steps

My future goals are to explore other quantum algorithms, such as **Grover's Algorithm,** and research what tasks or problems can be solved using quantum computing concepts. I seek to strengthen my conceptual and mathematical understanding of quantum computing through future exploration and experimentation.

---

## References

- IBM Quantum Learning: Basics of Quantum Information. [https://learning.quantum.ibm.com/course/basics-of-quantum-information](https://learning.quantum.ibm.com/course/basics-of-quantum-information)

- freeCodeCamp.org. (2024, May 15). _Quantum Computing Course - Math and Theory for Beginners_ [Video]. YouTube. [https://youtu.be/tsbCSkvHhMo?si=dq-VJe7bc9GSj-5p](https://youtu.be/tsbCSkvHhMo?si=dq-VJe7bc9GSj-5p)

- NumPy Documentation. [https://numpy.org/doc/](https://numpy.org/doc/)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

Brandon Fong

branfong21@gmail.com

[https://github.com/bfong-08](https://github.com/bfong-08)
