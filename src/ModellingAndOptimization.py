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
    # R is a submatrix of the markov chain which contains the transitions probabilities from transient states to absorbing states
    R = read_matrix(input("Please insert the file name containing the R matrix: "))
    # Q is a submatrix of the markov chain which contains the transitions probabilities from transient states to transient states
    Q = read_matrix(input("Please insert the file name containing the Q matrix: "))
    try:
        # I is the identity matrix
        I = np.identity(len(Q))
        # Calculate the difference between the inverse of the identity matrix and the Q matrix
        N = linalg.inv(I - Q)
        # Calculate the absorption probabilities by multiplying the N matrix by the R matrix
        NR = N @ R
        print(NR)
    except:
        print("Please insert a valid file name")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            absortion_probabilities()
        else:
            pass


def power_matrix():
    """
    Calculate the power of a matrix.

    The function reads a matrix and a power from the user, calculates the matrix raised to the specified power,
    and prints the result.
    """
    matrix = read_matrix(
        input("Please insert the file name containing the matrix: ")
    )
    try:
        power = int(input("Please insert the power: "))
        # Calculate the power of the matrix
        matrix = linalg.matrix_power(matrix, power)
        print(matrix)
    except linalg.LinAlgError:
        print("matrix is not square or power is not positive")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            power_matrix()
        else:
            pass
    except ValueError:
        print("Please insert a valid power")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            power_matrix()
        else:
            pass

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
        with open(filename, "r") as file:
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
        print("Please insert a valid file name")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            read_matrix(input("Please insert the file name containing the matrix: "))
        else:
            pass
    except ValueError:
        print("Please insert a valid file name")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            read_matrix(input("Please insert the file name containing the matrix: "))
        else:
            pass


def linear_equations_solver():
    """
    Solve a system of linear equations.

    Reads the equations system from a file, solves the system of linear equations,
    and prints the result.

    format of the file:
        3 4
        1 2 3 4
        4 5 6 7
        7 8 9 10

    this file represents the following system of linear equations:
        1x + 2y + 3z = 4
        4x + 5y + 6z = 7
        7x + 8y + 9z = 10
    """
    # equations_system is the matrix with the coefficients of the system of linear equations
    equations_system = read_matrix(
        input("Please insert the file name containing the equations system: ")
    )
    try:
        # A is the matrix of coefficients
        # The last column of the matrix is the matrix of constants so we remove it
        A = equations_system[:, :-1]
        # b is the matrix of constants, aka the last column of the matrix
        b = equations_system[:, -1]
        # b is a column vector
        #b = b_not.reshape(len(b_not), 1)
        # Calculate the solution of the system of linear equations
        x = linalg.solve(A, b)
        print("X = ",end="")
        print(x)
    except linalg.LinAlgError:
        print("this system of linear equations has either no solution or a unique solution")
        option = int(input("do you want to try again? (yes:1/no:0)"))
        if option == 1:
            read_matrix(input("Please insert the file name containing the matrix: "))
        else:
            pass

