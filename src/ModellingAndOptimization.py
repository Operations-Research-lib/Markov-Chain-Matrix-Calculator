import numpy as np
from numpy.linalg import linalg

# If True, always print floating point numbers using fixed point notation,
# in which case numbers equal to zero in the current precision will print as zero.
# If False, then scientific notation is used when absolute value of the smallest number
np.set_printoptions(suppress=True)


def absortion_probabilities():
    """This function will calculate the absorption probabilities of a markov chain"""
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
    '''This function will take in a matrix and a power and return the matrix to the power'''
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
    """This function will read a matrix from a file and return it as a 2 dimensional array
    format of the file:
    3 3
    0.5 0.5 0 
    0.25 0.5 0.25
    0 0.5 0.5
    The first line contains the row and column numbers of the matrix while the rest contains the values
    """
    try:
        with open(filename, 'r') as file:
            # Read the matrix dimensions from the first line of the file
            row, cols = map(int, file.readline().split())
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
