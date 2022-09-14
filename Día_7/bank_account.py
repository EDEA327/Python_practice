
#* Definición de las clases
from http import client


class Person:
    #* Constructor de la clase
    def __init__(self,name:str,last_name:str):
        self.name = name
        self.last_name = last_name

class Client(Person):
    #* Constructor de la clase
    def __init__(self,name,last_name,acc_number:int,balance:float = 0.0):
        super().__init__(name,last_name)
        self.acc_number = acc_number
        self.balance = balance

    #* Metodos
    def __str__(self):
        return f'''Client Information
        {"-"*50}
        Name: {self.name}
        Last Name: {self.last_name}
        Account Number: {self.acc_number}
        balance: {self.balance}
        {"-"*50}
        '''

    def deposit(self,amount:int):
        self.balance += amount
        print(f"Successfully Deposited {amount} $")
    def withdraw(self,amount:int):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Successfully Withdrwn {amount} $ ")
        else:
            print(f"You can't withdraw more than {self.balance} $")
#* Funciones

##* Funcíon para crear un  objeto de tipo cliente
def create_client():
    name = input("Please enter your name: ")
    last_name = input("Please enter your last name: ")
    acc_number = input("Please enter your acc_number: ")

    client = Client(name,last_name,acc_number)

    return client




##* Función de inicio
def main():

    my_client = create_client()
    print(my_client)

    menu = f""" Hi {my_client.name} Welcome! to your bank account
    What you want to do this time ? :
    1- Make a deposit
    2- Withdraw money
    3- Exit
    Please select an option: """

    keep_running = True
    while keep_running:
        option = int(input(menu))
        if option == 1:
            amount = int(input("How much money you want to deposit?: "))
            my_client.deposit(amount)
        elif option == 2:
            amount = int(input("How much you want to withdraw?: "))
            my_client.withdraw(amount)
        elif option == 3:
            break
        else:
            print("Please select a correct option.")
            continue
        print(my_client)
        wish = input("Want to continue? (y/n): ")
        if wish == "y":
            keep_running = True
        elif wish == "n":
            keep_running = False

#* Entrypoint
if __name__ == '__main__':
    main()