import sys 
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.quantum_simulator.quantum_state import QuantumState

# Function to choose each of the four oracle cases of U_f
def U_f(q: QuantumState, case: int):
    if case not in [1, 2, 3, 4]:
        raise ValueError("`case` must be 1, 2, 3, or 4")
    
    if case in [2, 3]:
        q.CNOT(0, 1)
    if case in [3, 4]:
        q.X(1)
    
# Initialize qubits $\ket{1}\otimes\ket{0}$
q = QuantumState([0, 0, 1, 0])

# Apply Hadamard layer
q.H(0)
q.H(1)

# Apply oracle function U_f
U_f(q, 4)

# Apply Hadamard to first qubit
q.H(0)

# Returns 0 if f is constant
# Returns 1 if f is balanced
print(q.measure(0))
