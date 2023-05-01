import ModellingAndOptimization as mo


def instructions():
    """
    Print the instructions for the menu.
    """
    print("\n--- Modelling and Optimization Calc ---")
    print("\nPress 0 to leave the menu")
    print("Press 1 to calculate absorption probabilities")
    print("Press 2 to calculate the power of a matrix")
    print("Press 3 to solve a equation system")
    print("Press 4 to find stable states")
    print("Press 5 to draw a graph of the markov chain\n")


def menu():
    """
    Display a menu to interact with the ModellingAndOptimization module.

    The menu provides options to calculate absorption probabilities or the
    power of a matrix.
    """
    answer = -1
    try:
        while answer != 0:
            instructions()
            answer = int(input("Answer: "))

            if answer == 1:
                # Call the function to calculate absorption probabilities here
                print("--- Absorption Probabilities ---")
                mo.absorption_probabilities()
            elif answer == 2:
                print("--- Power of a Matrix ---")
                # Call the function to calculate the power of a matrix here
                mo.power_matrix()
            elif answer == 3:
                print("--- Linear Equations Solver ---")
                # Call the function to solve a system of linear equations here
                mo.linear_equations_solver()
            elif answer == 4:
                print("--- Find Stable States ---")
                # Call the function to find stable states here
                mo.find_steady_states()
            elif answer == 5:
                print("--- Draw a Graph ---")
                # Call the function to draw a graph here
                mo.draw_markov_chain()
            elif answer == 0:
                print("Exiting the menu...")
            else:
                print("Invalid input. Please try again.")
    except ValueError:
        print("\n-ERROR: Invalid input. Exiting the menu-")
    except KeyboardInterrupt:
        print("\n-Kill signal received. Exiting the menu-")


if __name__ == "__main__":
    menu()
