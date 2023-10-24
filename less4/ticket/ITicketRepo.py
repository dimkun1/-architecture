from abc import ABC, abstractmethod

from Ticket import Ticket


class ITicketRepo(ABC):

    @abstractmethod
    def create_ticket(self, ticket: Ticket):
        ...

    @abstractmethod
    def read_ticket(self, ticket_id: int) -> Ticket:
        ...

    @abstractmethod
    def update_ticket(self, ticket_id: int, **kwargs) -> None:
        ...

    @abstractmethod
    def delete_ticket(self, ticket_id: int) -> bool:
        ...