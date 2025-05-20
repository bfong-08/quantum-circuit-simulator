import numpy as np
import numpy.typing as npt

def abs_squared(num: complex | float) -> npt.NDArray | float:
    """
    Returns the absolute value of a number squared.
    Used to find probabilities associated with
    outcomes of a quantum state

    Args:
        num (complex | float): the input

    Returns:
        npt.NDArray | float: the output
    """
    return np.abs(np.square(num))

def e_norm(vector: npt.NDArray) -> float | int:
    """
    Calculates the Euclidean norm of a vector. Used
    to ensure that a statevector has a Euclidean
    norm of 1.

    Args:
        vector (npt.NDArray): the statevector

    Returns:
        float | int: the Euclidean norm
    """
    return np.sum(abs_squared(vector))

def is_pow_of_2(length: int) -> bool:
    """
    Determines of a number is a power of 2, assuming
    that `length` > 0.

    Args:
        length (int): the input

    Returns:
        bool: true if the number is a power of 2; false otherwise
    """
    while length % 2 == 0:
        length //= 2
    return length == 1
