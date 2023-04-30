import numpy as np  # import the numpy module for arrays and matrix operations
from numpy.linalg import linalg  # import the linear algebra module from numpy

# set prints options for numpy arrays
# If True, always print floating point numbers using fixed point notation,
# in which case numbers equal to zero in the current precision will print as zero.
# If False, then scientific notation is used when absolute value of the smallest number
np.set_printoptions(suppress=True)


def absortion_probabilities():
    """
    Calculate the absorption probabilities of a Markov chain.

    The function reads the R and Q matrices from files, calculates the absorption probabilities,
    and prints the result.
    """
    try:
        # R is a submatrix of the markov chain which contains the transitions probabilities from transient states to absorbing states
        R = read_matrix(
            input('Please insert the file name containing the R matrix: '))
        # Q is a submatrix of the markov chain which contains the transitions probabilities from transient states to transient states
        Q = read_matrix(
            input('Please insert the file name containing the Q matrix: '))
        # I is the identity matrix
        I = np.identity(len(Q))
        # Calculate the difference between the inverse of the identity matrix and the Q matrix
        N = linalg.inv(I - Q)
        # Calculate the absorption probabilities by multiplying the N matrix by the R matrix
        NR = N @ R
        print(NR)
    except:
        print('Please insert a valid file name')
        absortion_probabilities()


def power_matrix():
    """
    Calculate the power of a matrix.

    The function reads a matrix and a power from the user, calculates the matrix raised to the specified power,
    and prints the result.
    """
    try:
        matrix = read_matrix(
            input('Please insert the file name containing the matrix: '))
        power = int(input('Please insert the power: '))
        # Calculate the power of the matrix
        matrix = linalg.matrix_power(matrix, power)
        print(matrix)
    except ValueError:
        print('Please insert a valid power')
        power_matrix()


def read_matrix(filename):
    """
    The file should have the following format:
    - The first line contains the number of rows and columns, separated by a space.
    - The subsequent lines contain the matrix values, with each row on a separate line and values separated by spaces.
    - format of the file:
        3 3
        0.5 0.5 0 
        0.25 0.5 0.25
        0 0.5 0.5
    Args:
        filename (str): The name of the file containing the matrix.

    Returns:
        np.ndarray: The matrix as a 2D NumPy array.
    """
    try:
        with open(filename, 'r') as file:
            # Read the matrix dimensions from the first line of the file
            row, cols = map(int, file.readline().split())
            # uses np.zeros to create a 2D array of zeros with the specified dimensions
            # it avoids mat because it is deprecated.
            matrix = np.zeros((row, cols))
            for i in range(row):
                row_data = file.readline().split()
                for j in range(cols):
                    matrix[i][j] = float(row_data[j])
        # Return matrix from file
        return matrix
    except FileNotFoundError:
        print('Please insert a valid file name')
        read_matrix(
            input('Please insert the file name containing the matrix: '))
    except ValueError:
        print('Please insert a valid file name')
        read_matrix(
            input('Please insert the file name containing the matrix: '))
