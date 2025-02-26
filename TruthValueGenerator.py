

'''
Written By: Yisehak Belay
Date of submission: 12/05/24
PROJECT FOR DISCRETE MATHEMATICS

The following program let's the user to choose the amount of statements the user wants to input which is limited to four in our case, then let's the user
to input the truth value of the statements after it outputs the result of five different logical operators based on the truth values the user input. In the
second choice the user can choose the number of statements which is limited to four in our case and the program outputs a truth table with five different logical
operators for the given number of statements.
'''
def logic_operations(variables):
    """
    This function perform logical operations AND, OR, NOT, XOR, and NAND
    on the provided boolean variables.
    """
    # It perform AND operation by checking if all statements have a truth value of TRUE
    and_result = all(variables)

    # It perform OR operation by checking if there is any variable with a truth value TRUE 
    or_result = any(variables)

    # It perform NOT operation by taking the opposite of each variable
    not_results = [not var for var in variables]



    #It perform XOR operation (True if an odd number of inputs are True)
    xor_result = False
    for var in variables:
        xor_result ^= var

    # It perform NAND operation (opposite of AND)
    nand_result = not and_result

    # Print the results for all operations
    print("P AND Q AND R AND S:", and_result)
    print("P OR Q OR R OR S:", or_result)
    print("NOT operation results:")
    for i, not_result in enumerate(not_results):
        print(f"NOT Variable {i+1}:", not_result)
    print("XOR operation result:", xor_result)
    print("NAND operation result:", nand_result)

def get_input():
    """
    This function to get input from the user for the logical variables.
    The number of variables (1-4) will be chosen by the user.
    """
    # Ask the user how many logical variables they want to input (1 to 4)
    num_variables = int(input("How many variables would you like to input (1 to 4)? ").strip())

    if num_variables < 1 or num_variables > 4:
        print("Invalid choice! Please choose a number between 1 and 4.")
        return get_input()

    # Initialize the list of variables
    variables = []

    # Prompt the user to enter the values (True or False) for each variable
    for i in range(num_variables):
        var_input = input(f"Enter value for variable {i+1} (True/False): ").strip().lower()
        variables.append(var_input == "true")

    # Call the above function to perform logic operations
    logic_operations(variables)

def truth_table():
    """
    This function generate and print the truth table for all combinations of variables.
    The number of variables (1 to 4) will be determined by the user.
    """
    # Ask the user how many variables to use in the truth table (1 to 4)
    num_variables = int(input("Choose the number of statement for your truth table (1 to 4)? ").strip())

    if num_variables < 1 or num_variables > 4:
        print("Invalid choice! Please choose a number between 1 and 4.")
        return truth_table()

    # Print the header of the truth table(the variables and the operators)
    header = "\t".join([f"Var{i+1}" for i in range(num_variables)]) + "\tAND\tOR\tXOR\tNAND"
    print("Generating truth table for", num_variables, "variables:")
    print(header)

    # The following loop generate all combinations of variables (2 possibilities per variable) and repeats based on the number of variables
    for values in product([True, False], repeat=num_variables):
        and_result = all(values)
        or_result = any(values)
        not_results = [not val for val in values]
        xor_result = False
        for val in values:
            xor_result ^= val
        nand_result = not and_result

        # Print the results for this combination in a tabular format
        print("\t".join([str(val) for val in values]) + f"\t{and_result}\t{or_result}\t{xor_result}\t{nand_result}")
        
#The following statement where itertools is from the python library which helps to get the cartesian product of two lists
from itertools import product

def main():
    """
    This is the Main function to drive the program.
    The user is prompted to choose between generating a truth table or inputting custom values for variables.
    """
    # Asking the user for their choice of operation
    choice = input("Choose option:\n1. Input values for variables\n2. Generate truth table\nEnter 1 or 2: ").strip()
    
    # If user chooses option 1, call get_input function
    if choice == '1':
        get_input()
    # If user chooses option 2, call truth_table function
    elif choice == '2':
        truth_table()
    else:
        # If user enters an invalid choice, prompt again
        print("Invalid choice! Please run the program again.")

# Calling the main function to run the program
if __name__ == "__main__":
    main()


