import numpy as np
import numpy.typing as npt

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
