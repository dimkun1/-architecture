class BankAccount:

    def __init__(self, card: int, balance: float = 0) -> None:
        self.__card = card
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float) -> None:
        self.__balance = balance

    @property
    def card(self) -> int:
        return self.__card