from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class MyBankATM(ATM):

    def withdraw(self):
        self.__verify_pin()
        self.__check_balance()
        self.__update_server()
        print("Cash withdrawn successfully..")

    def __verify_pin(self):
        print("Pin Verified")

    def __check_balance(self):
        print("Balance Checked")

    def __update_server(self):
        print("Server Updated")

atm = MyBankATM()
atm.withdraw()