"""
    This program works as a shift assigner for a pharmacy that sells cosmetics, medicines and perfumes.
"""
# imports
import functions
from os import system
# Global variables

MENU = """Welcome to your favorite pharmacy
Please select a category to take your shift...
C-Cosmetics
P-Pharmacy
Pe-Perfumery
Please select an option: """

# Function definitions

def choose_category():
    """_This function ask for the category selected by user_
    """

    while True:
        try:
            category = input(MENU).capitalize()
            ["C","P","Pe"].index(category)
        except ValueError:
            print("Thats is not a valid category")
        else:
            break

    functions.decorator(category)



def run():
    """ The main function for this program. """

    # Se le pide al usuario que escoja una categoria
    while True:
        choose_category()
        try:
            shift = input("Want another shift? (y/n): ").lower().strip()
            ["y","n"].index(shift)
            system("cls")
        except ValueError:
            print("Invalid")
            system("cls")
        else:
            if shift == "n":
                print("Thanks for your visit come back soon.")
                break


if __name__ == '__main__':
    run()