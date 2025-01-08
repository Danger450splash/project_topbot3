
from abc import ABC, abstractmethod
import os

class AbstractClass(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def program(self):
        pass


class AutomaticMachineTeller(AbstractClass): # Class Instance

    def __init__(self) -> None: # Constructor
        self.program()
        self.__loopPattern()
        self.__comprehension()
        # Instance Variables
        self.__balance: int = 5000
        self.__userBudget: int = 1000
        self.__menu()

    def program(self):
        print(f'ATM Program Activated.')
        print(f'You are now in control.')

    def __menu(self) -> None: # Instance Method 1
        print("\n")
        print(f'Budget: {self.__userBudget}')
        print(f'Welcome to RavenBank')
        print(f'[1] - Check Balance')
        print(f'[2] - Deposit')
        print(f'[3] - Withdraw')
        print(f'[0] - Cancel')

        __userinput = int(input("Select from [0] to [3]: "))
        self.__userinputChecker(__userinput)

    def __userinputChecker(self, index: int) -> int: # Instance Method 1.1
        self.__index: int = index

        if self.__index == 0:
            print(f'User cancelled, have a nice day!')

        elif self.__index == 1:
            self.__userAccount()

        elif self.__index == 2:
            os.system('cls')
            __userinputD = int(input("Enter Deposit Amount: "))
            self.__deposit(__userinputD)

        elif self.__index == 3:
            self.__withdraw()

        else:
            print(f'Try again')
            self.__menu()

        return None





    def __userAccount(self) -> None: # Instance Method 2
        os.system('cls')
        print(f'=============================')
        print(f'ATM Balance: {self.__balance}')
        print(f'=============================')
        self.__menu()

    def __deposit(self, amountD: int) -> int: # Instance Method 3
        os.system('cls')
        self.__amountD: int = amountD

        if self.__amountD <= self.__userBudget:
            os.system('cls')
            self.__userBudget: int = self.__userBudget - self.__amountD
            self.__balance: int = self.__balance + self.__amountD
            print(f'Successfullly Deposited - New Balance: {self.__balance}')
            print(f'You only have {self.__userBudget} in your pocket.')
            self.__menu()
        else:
            os.system('cls')
            print(f"You don't have enough budget to deposit into your ATM.")
            print(f"You're depositing an amount that is not equal or greater in your current budget.")
            self.__menu()

        return None

    def __withdraw(self) -> None: # Instance Method 4
        os.system('cls')
        print(f'Current ATM Balance: {self.__balance}')
        __userinputW = int(input("Enter the Amount of Withdraw: "))

        if __userinputW <= self.__balance:
            os.system('cls')
            self.__balance = self.__balance - __userinputW
            self.__userBudget = self.__userBudget + __userinputW
            print(f'Successfully Withdrawed - New Budget: {self.__userBudget}')
            print(f'You only have {self.__balance} in your ATM Balance.')
            self.__menu()
        else:
            os.system('cls')
            print(f"You don't have enough balance to do a withdraw from your ATM.")
            print(f"You're withdrawing an amount that is not equal or greater in your current ATM Balance.")
            self.__menu()



    def __loopPattern(self) -> None:
        __stars = 5

        for __rows in range(1, __stars+1):
            __num = 1
            for __columns in range(__stars+1, 0, -1):
                if __columns > __rows:
                    print(" ", end=' ')
                else:
                    print("*", end=' ')
                    __num += 1
            print()

    def __comprehension(self) -> None:
        __names = ["Alpha", "Bravo", "Charlie", "Delta"]
        __listComprehension = [{__x for __x in __names}]
        print(__listComprehension)


# Instance Object of the Class
ATM: AutomaticMachineTeller = AutomaticMachineTeller()