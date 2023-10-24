from datetime import datetime

from Ticket import Ticket
from ITicketRepo import ITicketRepo


class TicketRepository(ITicketRepo):

    __ticket_repository: list[Ticket] = []

    def __init__(self) -> None:
        pass

    @property
    def repository(self) -> list[Ticket]:
        return self.__ticket_repository

    def create_ticket(self, ticket: Ticket):
        self.__ticket_repository.append(ticket)

    def read_ticket(self, date_time: datetime) -> list[Ticket]:
        return [ticket for ticket in self.__ticket_repository if ticket.date_time == date_time]

    def update_ticket(self, ticket_id: int, **kwargs) -> bool:
        for ticket in self.__ticket_repository:
            if ticket.id == ticket_id:
                ticket.set_valid = True
                return True
        return False

    def delete_ticket(self, ticket_id: int) -> bool:
        for ticket in self.__ticket_repository:
            if ticket.id == ticket_id:
                self.__ticket_repository.remove(ticket)
                return True
        return False