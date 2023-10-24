from ICashRepo import ICashRepo

from BankAccount import BankAccount


class CashRepository(ICashRepo):
    __clients: list[BankAccount] = []

    def __init__(self) -> None:
        pass

    @property
    def clients(self) -> list[BankAccount]:
        return self.__clients

    def transaction(self, bank_account: BankAccount, cost: float) -> bool:
        if bank_account.balance >= cost:
            bank_account.balance -= cost
            return True
        return False