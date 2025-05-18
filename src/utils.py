import numpy as np
import numpy.typing as npt
from random import random

def abs_squared(num: complex | float):
    return np.abs(np.square(num))

def e_norm(vector: npt.NDArray):
    return np.sum(abs_squared(vector))

def is_pow_of_2(length: int):
    while length % 2 == 0:
        length //= 2
    return length == 1

class Operator:
    def __init__(self, matrix: npt.NDArray | list):
        matrix = np.array(matrix, dtype=complex)
        if matrix.shape[0] != matrix.shape[1]:
            raise Exception("The operation must be a square matrix")
        if not np.allclose((matrix @ np.conjugate(matrix).T), np.identity(matrix.shape[0]), atol=1e-5):
            raise Exception("The operation must be a unitary matrix")
        self.operation = matrix
    
    def to_numpy(self):
        return self.operation
    
    def __str__(self):
        return str(self.operation.round(4))

class QuantumState:
    def __init__(self, statevector: npt.NDArray):
        if not is_pow_of_2(len(statevector)):
            raise Exception("The length of the statevector must be a power of 2")
        if abs(1 - e_norm(statevector)) > 1e-5:
            raise Exception("The Euclidean norm of the state must be 1")
        
        self.state = np.array(statevector, dtype=complex)
        self.n_qubits = round(np.log2(len(statevector)))

    def __str__(self):
        return self.state.round(4).__str__()
    
    def add_qubit(self, qubit: 'npt.NDArray | QuantumState'):
        if isinstance(qubit, QuantumState):
            q = qubit.to_numpy()
            self.state = np.kron(self.state, q)
            self.n_qubits += round(np.log2(len(q)))
        else:
            self.state = np.kron(self.state, qubit)
            self.n_qubits += round(np.log2(len(qubit)))
    
    def measure(self, index: int):
        if index < 0 or index >= self.n_qubits:
            raise Exception(f"Qubit index {index} is out of range for {self.n_qubits} qubits")

        index = self.n_qubits - index - 1
        probs = np.abs(np.square(self.state))

        prob_0 = sum(probs[i] for i in self.get_qubit_indices(index, 0))
        result = 0 if random() < prob_0 else 1

        indices = self.get_qubit_indices(index, result)
        mask = np.zeros_like(self.state)
        mask[indices] = 1
        self.state *= mask
        self.state /= np.sqrt(sum(probs[indices]))
        return result

    def get_qubit_indices(self, index: int, outcome: int):
        indices = []
        for i in range(len(self.state)):
            bits = format(i, f'0{self.n_qubits}b')
            if int(bits[index]) == outcome:
                indices.append(i)
        return indices
    
    def CNOT(self, control: int, target: int):
        control = self.n_qubits - control - 1
        target = self.n_qubits - target - 1
        new_state = np.zeros_like(self.state)
        for i in range(len(self.state)):
            b = format(i, f'0{self.n_qubits}b')
            if b[control] == '1':
                flipped = list(b)
                flipped[target] = '0' if b[target] == '1' else '1'
                j = int(''.join(flipped), 2)
                new_state[j] += self.state[i]
            else:
                new_state[i] = self.state[i]
        self.state = new_state
        
    def X(self, index: int):
        index = self.n_qubits - index - 1
        x = np.array([
            [0, 1],
            [1, 0]
        ])
        operator = self.__expand_operator(index, x)
        self.state = operator @ self.state

    def Z(self, index: int):
        index = self.n_qubits - index - 1
        z = np.array([
            [1, 0],
            [0, -1]
        ])
        operator = self.__expand_operator(index, z)
        self.state = operator @ self.state

    def H(self, index: int):
        index = self.n_qubits - index - 1
        h = np.array([
            [1, 1],
            [1, -1]
        ]) / np.sqrt(2)
        operator = self.__expand_operator(index, h)
        self.state = operator @ self.state

    def __expand_operator(self, index: int, operation: npt.NDArray):
        i_2 = np.identity(2)
        if index == 0:
            operator = operation
        else:
            operator = i_2
        for i in range(1, self.n_qubits):
            if i == index:
                operator = np.kron(operator, operation)
            else:
                operator = np.kron(operator, i_2)
        return operator

    def to_numpy(self):
        return self.state
