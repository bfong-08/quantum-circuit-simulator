import numpy as np
import numpy.typing as npt
from random import random
from .utils import is_pow_of_2, e_norm

class QuantumState:
    def __init__(self, statevector: npt.NDArray):
        """
        Represents a quantum state through a statevector

        Args:
            statevector (npt.NDArray): the initial quantum state

        Raises:
            Exception: the state vector's length must be a power of 2
            Exception: the Euclidean norm of the state must be 1
        """

        if not is_pow_of_2(len(statevector)):
            raise Exception("The length of the statevector must be a power of 2")
        if abs(1 - e_norm(statevector)) > 1e-5:
            raise Exception("The Euclidean norm of the state must be 1")
        
        self.state = np.array(statevector, dtype=complex)
        self.n_qubits = round(np.log2(len(statevector)))

    def __str__(self):
        return self.state.round(4).__str__()
    
    def __getitem__(self, index):
        return self.state[index]

    def __len__(self):
        return self.state.size
    
    @classmethod
    def from_qubits(self, *qubits: 'npt.NDArray | QuantumState') -> 'QuantumState':
        """
        Constructs a quantum state from a list of n qubits

        Returns:
            QuantumState: an instance of the `QuantumState` class
        """
        statevector = np.array([1], dtype=complex)
        for qubit in qubits:
            if isinstance(qubit, QuantumState):
                statevector = np.kron(statevector, qubit.to_numpy())
            else:
                statevector = np.kron(statevector, qubit)

        return self(statevector)

    def add_qubit(self, qubit: 'npt.NDArray | QuantumState'):
        """
        Adds a qubit to a quantum state using the tensor product

        Args:
            qubit (npt.NDArray | QuantumState): the qubit to be added to the quantum state
        """
        if isinstance(qubit, QuantumState):
            q = qubit.to_numpy()
            self.state = np.kron(self.state, q)
            self.n_qubits += round(np.log2(len(q)))
        else:
            self.state = np.kron(self.state, qubit)
            self.n_qubits += round(np.log2(len(qubit)))
    
    def measure(self, index: int) -> int:
        """
        Performs a partial measurement on a quantum state, 
        updating the state according to the measurement outcome

        Args:
            index (int): the index of the qubit to be measured

        Raises:
            Exception: the index must correspond to an existing qubit

        Returns:
            int: the result of the measurement
        """
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

    def get_qubit_indices(self, index: int, outcome: int) -> list[int]:
        """
        Retrieves the indices of the statevector 
        that contain the specified outcome
        of the qubit in the specified index

        Args:
            index (int): the index of the qubit
            outcome (int): the qubit's desired state (0, 1)

        Returns:
            list[int]: the indices of the statevector
        """
        indices = []
        for i in range(len(self.state)):
            bits = format(i, f'0{self.n_qubits}b')
            if int(bits[index]) == outcome:
                indices.append(i)
        return indices
    
    def CNOT(self, control: int, target: int):
        """
        Performs a controlled NOT gate on two specified qubits,
        leaving all other qubits unchanged

        Args:
            control (int): the index of the control qubit
            target (int): the index of the target qubit
        """
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
        """
        Performs a bit flip on the specified qubit,
        leaving all other qubits unchanged

        Args:
            index (int): the index of the target qubit
        """
        index = self.n_qubits - index - 1
        x = np.array([
            [0, 1],
            [1, 0]
        ])
        operator = self.__expand_operator(index, x)
        self.state = operator @ self.state

    def Z(self, index: int):
        """
        Performs a phase flip on the specified qubit,
        leaving all other qubits unchanged

        Args:
            index (int): the index of the target qubit
        """
        index = self.n_qubits - index - 1
        z = np.array([
            [1, 0],
            [0, -1]
        ])
        operator = self.__expand_operator(index, z)
        self.state = operator @ self.state

    def H(self, index: int):
        """
        Performs a Hadamard gate on the specified qubit,
        leaving all other qubits unchanged

        Args:
            index (int): the index of the target qubit
        """
        index = self.n_qubits - index - 1
        h = np.array([
            [1, 1],
            [1, -1]
        ]) / np.sqrt(2)
        operator = self.__expand_operator(index, h)
        self.state = operator @ self.state

    def __expand_operator(self, index: int, operation: npt.NDArray) -> npt.NDArray:
        """
        Expands an operator to NxN dimensions where N is the 
        length of the statevector. The new operator will only
        affect the qubit of the specified index, leaving all
        other qubits unchanged. It does this by finding the 
        tensor products of identity matrices and the operation,
        where the order corresponds to the specified index

        Args:
            index (int): the index of the target qubit
            operation (npt.NDArray): the operation to be performed on the target qubit

        Returns:
            npt.NDArray: the new expanded operator
        """
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

    def to_numpy(self) -> npt.NDArray:
        """
        Returns the statevector as an NDArray

        Returns:
            npt.NDArray: the statevector
        """
        return self.state
