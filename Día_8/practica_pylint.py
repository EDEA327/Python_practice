'''
This module contains a simple function that sum
2 numbers
'''


def add(num_1:int, num_2:int) -> int:
    """_This function receive two integer  numbers as parameters
    and sum it_

    Parameters
    ----------
    num_1 : int
        _An integer number_
    num_2 : int
        _An integer number_

    Returns
    -------
    int
        _The result of num_1 + num_2_
    """

    return num_1+num_2


def run():
    """_The main function of the module_
    """
    suma = add(5, 7)

    print(f"The result was : {suma}")


if __name__ == "__main__":
    run()
