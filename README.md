# Quantum Teleportation Protocol with NumPy

Quantum teleportation allows the transfer of an unknown quantum state from one location to another using **entanglement** and **classical communication** without physically sending the qubit itself. This process is important because it is a reliable way to transmit quantum data securely and accurately without measuring the quantum state or violating the **no-cloning theorem.** Quantum teleportation is essential for building quantum networks, distributed quantum computers, and the quantum internet.

## Goals

- Understand and implement the **quantum teleportation protocol**
- Explore how **entanglement** and **measurement** affect quantum systems
- Simulate key quantum gates: **Hadamard**, **CNOT**, **Pauli-X**, and **Pauli-Z**
- Simulate **partial measurements** of entangled systems
- Gain insight into how quantum states are represented and evolve

---

## Project Structure

- [notebooks/](.\quantum-teleportation-project\notebooks)
  - [prototype.ipynb](.\quantum-teleportation-project\notebooks\prototype.ipynb)
- [src/](.\quantum-teleportation-project\src)
  - [main.py](.\quantum-teleportation-project\src\main.py)
  - [utils.py](.\quantum-teleportation-project\src\utils.py)
- [.gitignore](.\quantum-teleportation-project.gitignore)
- [LICENSE](.\quantum-teleportation-project\LICENSE)
- [README.md](.\quantum-teleportation-project\README.md)
- [requirements.txt](.\quantum-teleportation-project\requirements.txt)

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/bfong-08/quantum-teleportation-project.git
cd quantum-teleportation-project
```

2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the simulation

```bash
python main.py
```

5. (Optional) Open the notebook for exploration

```bash
jupyter notebook notebooks/prototype.ipynb
```

You should see the full protocol simulated step-by-step, including:

- Initial entangled state
- Measurement outcomes
- Conditional gate corrections
- Final comparison between Bob's qubit and the original unknown state

## Key Concepts

- **Qubits** as complex state vectors
- **Entanglement** via the Hadamard and CNOT gates (resulting in a bell state)
- **Quantum measurement** and **state collapse**
- **Classical communication** to complete teleportation
- **Custom implementation** of state evolution (no Qiskit involved)

## What I Learned

While building this, I deepened my understanding of quantum state manipulation, gate operations, and how measurement impacts entangled systems. This project helped me gain confidence in applying quantum concepts using Python, and it is my first major step into the world of quantum computing.
