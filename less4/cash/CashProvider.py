from ticket.Ticket import Ticket
from user.User import User
from CashRepository import CashRepository


class CashProvider:
    __cash_repository = CashRepository()

    def __init__(self) -> None:
        pass

    def authorization(self, user: User) -> bool:
        if user.bank_account.card in self.__cash_repository.clients:
            return True
        return False

    def buy_ticket(self, ticket: Ticket, user: User) -> bool:

        # Предусловие
        assert self.authorization(user) == True

        if user.bank_account.balance >= ticket.price:
            return True
        return False