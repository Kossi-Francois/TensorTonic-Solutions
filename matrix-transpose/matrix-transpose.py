import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    # let A, B € R^(n*m), and C € R^(m*k), p, q € R
    # (A^T)ij = Aji, st. A^T € R^(m*n)
    # (A^T)^T = A
    # (p.A + B)^T = p.(A^T) + B^T
    # (A.C)^T = ( C^T . A^T ) € R^(k*n)
    # if A is symmetry (meaning Aij = Aji ) <==> A = A^T
    n, m = len(A), len(A[0])
    A_T = np.asarray([  [  A[row][col]  for row in range(n)  ] for col in range(m)   ])
    
    return A_T
    
