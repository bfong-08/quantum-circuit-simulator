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

class Qubit:
    def __init__(self, alpha: complex, beta: complex):
        if abs(1 - e_norm([alpha, beta])) > 1e-5:
            raise Exception("The Euclidean norm of the state must be 1")
        
        self.alpha = alpha
        self.beta = beta

    def __str__(self):
        return f"{self.alpha:.4f}|0⟩ + {self.beta:.4f}|1⟩"
    
    def measure(self):
        if random() < abs_squared(self.alpha):
            self.alpha = 1
            self.beta = 0
            return 0
        else:
            self.alpha = 0
            self.beta = 1
            return 1
        
    def evolve(self, operator: Operator):
        operator = operator.to_numpy()
        if operator.shape != (2, 2):
            raise Exception(f"The operator's shape {operator.shape} is incompatible with the qubit")
        state = np.array([self.alpha, self.beta])
        transformed = operator @ state
        self.alpha = transformed[0]
        self.beta = transformed[1]

    def to_numpy(self):
        return np.array([self.alpha, self.beta])
        