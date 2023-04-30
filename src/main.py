import ModellingAndOptimization as mo


def instructions():
    print('Press 0 to leave the menu')
    print('Press 1 to calculate absorption probabilities')
    print('Press 2 to calculate the power of a matrix')


def menu():
    answer = -1
    while answer != 0:
        instructions()
        answer = int(input('Answer: '))

        if answer == 1:
            # Call the function to calculate absorption probabilities here
            print("--- Absorption Probabilities ---")
            mo.absorption_probabilities()
        elif answer == 2:
            print("--- Power of a Matrix ---")
            # Call the function to calculate the power of a matrix here
            mo.power_matrix()
        elif answer == 0:
            print("Exiting the menu...")
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    menu()
