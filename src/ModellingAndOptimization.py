import numpy as np  # import the numpy module for arrays and matrix operations
from numpy.linalg import (
    linalg as linearAlgebra,
)  # import the linear algebra module from numpy
import networkx as nx
import matplotlib.pyplot as plt

# set prints options for numpy arrays
# If True, always print floating point numbers using fixed point notation,
# in which case numbers equal to zero in the current precision will print as zero.
# If False, then scientific notation is used when absolute value of the smallest number
np.set_printoptions(suppress=True)


def absorption_probabilities():
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
        N = linearAlgebra.inv(I - Q)
        # Calculate the absorption probabilities by multiplying the N matrix by the R matrix
        NR = N @ R
        print(NR)
    except:
        print("-ERROR: Please insert a valid file name")
        option = int(input("- do you want to try again? (yes:1/no:0): "))
        if option == 1:
            absorption_probabilities()
        else:
            pass


def power_matrix():
    """
    Calculate the power of a matrix.

    The function reads a matrix and a power from the user, calculates the matrix raised to the specified power,
    and prints the result.
    """
    matrix = read_matrix(input("Please insert the file name containing the matrix: "))
    try:
        power = int(input("Please insert the power: "))
        # Calculate the power of the matrix
        matrix = linearAlgebra.matrix_power(matrix, power)
        print(matrix)
    except linearAlgebra.LinAlgError:
        print("matrix is not square or power is not positive")
        option = int(input("- do you want to try again? (yes:1/no:0): "))
        if option == 1:
            power_matrix()
        else:
            pass
    except ValueError:
        print("-ERROR: Please insert a valid power")
        option = int(input("- do you want to try again? (yes:1/no:0): "))
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
    except:
        print("-ERROR: Please insert a valid file name")
        option = int(input("- do you want to try again or exit()? (yes:1/no:0): "))
        if option == 1:
            read_matrix(input("Please insert the file name containing the matrix: "))
        else:
            exit()


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
        # b = b_not.reshape(len(b_not), 1)
        # Calculate the solution of the system of linear equations
        x = linearAlgebra.solve(A, b)
        print("X = ", end="")
        print(x)
    except linearAlgebra.LinAlgError:
        print(
            "-ERROR: this system of linear equations has either no solution or no unique solution"
        )
        option = int(
            input("- do you want to try again with another matrix? (yes:1/no:0): ")
        )
        if option == 1:
            linear_equations_solver()
        else:
            pass


def find_steady_states():
    """
    This function reads a Markov chain transition matrix from a file,
    calculates its steady-state vector, and prints the result.
    If there is a problem with the linear system (e.g., no unique solution),
    the function provides an option to try again with another matrix.
    """
    transition_matrix = read_matrix(
        input("Please insert the file name containing the transition matrix: ")
    )
    # M is the number of states
    M = transition_matrix.shape[0]
    try:
        # to compute the steady-state vector, we need to solve a linear system
        # πj = ∑(M, i=0) πi*pij
        # Transpose the matrix and subtract the identity matrix
        A = np.transpose(transition_matrix) - np.identity(M)
        # Append a row of ones to the matrix_diff
        A = np.append(A, np.ones((1, M)), axis=0)
        # Solve the linear system  Ax = b where x is the steady state vector
        b = np.zeros(M)
        b = np.append(b, 1)
        # Use the least-squares method to solve the linear system
        # matrix_diff * steady_state = b for the steady_state vector.
        # lstsq() returns a tuple, and the first element ([0]) contains the solution.
        # rcond=None is set for using the default machine precision for the conditioning of the matrix.
        pi = linearAlgebra.lstsq(A, b, rcond=None)[0]
        # Print the steady state vector
        print("pi = ", end="")
        print(pi)
    except linearAlgebra.LinAlgError:
        print(
            "-ERROR: this system of linear equations made to calculate stables states has either no solution or a no unique solution"
        )
        option = int(
            input("- do you want to try again with another matrix? (yes:1/no:0): ")
        )
        if option == 1:
            find_steady_states()
        else:
            pass


def read_markov_chain_to_graph(filename):
    with open(filename, "r") as file:
        # Read the first line, strip leading/trailing whitespaces,
        # split the values and convert them to integers
        rows, cols = map(int, file.readline().strip().split())

        # Read the second line, strip leading/trailing whitespaces, and split the state labels
        state_labels = file.readline().strip().split()
        transition_matrix = np.zeros((rows, cols))
        for i in range(rows):
            row_data = file.readline().split()
            for j in range(cols):
                transition_matrix[i][j] = float(row_data[j])
    return transition_matrix, state_labels


def draw_markov_chain():
    """
    This function reads a Markov chain from a file, creates a weighted directed graph using the NetworkX library,
    and visualizes the graph with node and edge labels. The input file should contain the transition matrix and
    state labels of the Markov chain.
    format of the file:

    4 4
    I T D R
    0.05 0.93 0.02 0
    0.1 0.86 0.04 0
    0 0 0.8 0.2
    0.5 0.1 0 0.4

    where the first line contains the number of rows and columns of the transition matrix,
    the second line contains the state labels, and the remaining lines contain the transition matrix.
    Limitations: self pointing edges are do not show weights.
    """
    # Prompt the user to input the file name containing the transition matrix
    filename = input("Please insert the file name containing the transition matrix: ")
    # Try to open the file and read its contents
    try:
        transition_matrix, state_labels = read_markov_chain_to_graph(filename)
        # Initialize a directed graph object
        G = nx.DiGraph()
        # Iterate through the state labels and their indices
        for i, state in enumerate(state_labels):
            # for each state, add a node to the graph
            G.add_node(state)
            # Iterate through the transition probability in the
            # transition matrix row corresponding to the current state
            for j, transition_probability in enumerate(transition_matrix[i]):
                # for each transition_probability that is greater than zero, add
                # a weighted edge to the graph
                if transition_probability > 0:
                    G.add_edge(state, state_labels[j], weight=transition_probability)
        # Create using circular layout for the graph
        pos = nx.circular_layout(G)
        # Draw the graph with nodes and labels
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2000,
            node_color="skyblue",
            font_weight="bold",
        )
        # Get the edge attributes (weights) from the graph
        edge_labels = nx.get_edge_attributes(G, "weight")
        # Draw the edge labels on the graph
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=10
        )
        # Display the graph
        plt.show()
    except FileNotFoundError:
        print("-ERROR: Please insert a valid file name")
        option = int(input("- do you want to try again or exit()? (yes:1/no:0): "))
        if option == 1:
            draw_markov_chain(
                input("Please insert the file name containing the Markov chain: ")
            )
        else:
            pass
    except IndexError:
        print("-ERROR: Please insert a matrix with the correct dimensions")
        option = int(input("- do you want to try again or exit()? (yes:1/no:0): "))
        if option == 1:
            draw_markov_chain()
        else:
            pass
    except Exception as e:
        print("-ERROR: ", e)
        option = int(input("- do you want to try again or exit()? (yes:1/no:0): "))
        if option == 1:
            draw_markov_chain()
        else:
            pass
