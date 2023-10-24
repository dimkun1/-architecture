from abc import ABC, abstractmethod
from datetime import datetime

from ticket.Ticket import Ticket
from user.User import User

class ICustomer(ABC):

    @abstractmethod
    def search_ticket(id: int, date_time: datetime) -> list[Ticket]:
        ...

    @abstractmethod
    def buy_ticket(ticket: Ticket) -> bool:
        ...