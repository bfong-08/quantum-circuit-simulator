from quantum_simulator.quantum_state import QuantumState
import numpy as np

# Alice's qubit
A = np.array([1, 0])

# Bob's qubit
B = np.array([1, 0])

# Entangle the qubits
state = QuantumState.from_qubits(B, A)
state.H(0)
state.CNOT(0, 1)

# Bell state
print(f"Bell state (B, A): {state}\n")

# Alice's unknown qubit
Q = np.array([0.5, np.sqrt(3)/2], dtype=complex)
print(f"Q: {Q.round(4)}\n")

state.add_qubit(Q)
print(f"(B, A, Q) before protocol: {state}\n")

# Begin teleportation protocol
state.CNOT(0, 1)
state.H(0)

Q_measurement = state.measure(0)
A_measurement = state.measure(1)

print("Measurements: {", f"A: {A_measurement} | Q: {Q_measurement}", "}\n")

print(f"(B, A, Q) before correction: {state}\n")

if A_measurement == 1:
    state.X(2)

if Q_measurement == 1:
    state.Z(2)

# Final state
print(f"(B, A, Q) after protocol: {state}\n")

# Isolate Bob's qubit
B = np.array([
    np.sum(state.to_numpy()[:4]),
    np.sum(state.to_numpy()[4:])
], dtype=complex)
print(f"Alice's initial unknown qubit: {Q.round(4)}")
print(f"Bob's qubit after protocol: {B.round(4)}")
