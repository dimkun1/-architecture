from abc import ABC, abstractmethod

from BankAccount import BankAccount


class ICashRepo(ABC):

    @abstractmethod
    def transaction(self, bank_account: BankAccount, cost: float) -> bool:
        ...