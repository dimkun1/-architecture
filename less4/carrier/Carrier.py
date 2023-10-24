from cash.BankAccount import BankAccount


class Carrier:

    def __init__(self, id: int, places: list[int], bank_account: BankAccount) -> None:
        self.__id = id
        self.__places = places
        self.__bank_account = bank_account

    @property
    def id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    @property
    def places(self) -> list[int]:
        return self.__places

    def set_places(self, id: int, status: bool) -> None:
        if status:
            self.__places.remove(id)
        else:
            self.__places.add(id)

    @property
    def bank_account(self) -> BankAccount:
        return self.__bank_account

    def set_bank_account(self, bank_account: BankAccount) -> None:
        self.__bank_account = bank_account